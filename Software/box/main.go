package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"io"
	"io/ioutil"
	"os"
	"os/exec"
	"regexp"
	"strconv"
	"time"
)

const (
	scriptPwm string = "./pwm_control.py"
	fileName  string = "box_log.csv"
)

func main() {
	// scriptPwm := "./pwm_control.py"
	//初始设置
	config := readConfig()
	setup(scriptPwm, config)
	tempreture, pressure, humidity := getAir()
	light := getLight()
	r := gin.Default()
	r.GET("/servo1", func(c *gin.Context) {
		ChangeMode(scriptPwm, config.PinSERVO, "0", "SERVO")

	})
	r.GET("/servo2", func(c *gin.Context) {
		ChangeMode(scriptPwm, config.PinSERVO, "90", "SERVO")

	})
	r.GET("/config", func(c *gin.Context) {
		readConfig()

	})
	go loop2(tempreture, pressure, humidity, light)
	r.Run(":8081")

}

func getLine(fileName string) []string {

	fs, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("can not open the file, err is %+v", err)
	}
	defer fs.Close()

	r := csv.NewReader(fs)
	r.FieldsPerRecord = -1
	//针对大文件，一行一行的读取文件
	var row2 []string
	for {
		row1, err := r.Read()
		if err != nil && err != io.EOF {
			fmt.Printf("can not read, err is %+v", err)
		}
		if err == io.EOF {
			break
		}
		row2 = row1
	}
	return row2
}

func loop2(tempreture, pressure, humidity float64, light int) {

	line := getLine(fileName)
	num, err := strconv.Atoi(line[0])
	if err != nil {
		num = 0
	}

	for i := num + 1; ; i++ {
		go loop(tempreture, pressure, humidity, light, i)
		time.Sleep(time.Second * 5)
	}
}
func loop(tempreture, pressure, humidity float64, light, num int) {
	tempreture, pressure, humidity = getAirStable()
	light = getLightStable()

	//code here
	//根据气压、温度、湿度决定两个风扇的风速
	//监控内部亮度，改变亮度

	//此处记录各传感器数值
	var cstSh, _ = time.LoadLocation("Asia/Shanghai")
	now := time.Now().In(cstSh).Format("2006-01-02 15:04:05")
	fmt.Println(now)
	fmt.Println("Tempreture:", tempreture)
	fmt.Println("Pressure:", pressure)
	fmt.Println("Humidity:", humidity)
	fmt.Println("Light:", light)
	writeLog(tempreture, pressure, humidity, light, num)
	/*
		需要写一个函数判断是否需要改变风扇转速、LED灯亮度等。

	*/
}

func writeLog(tempreture, pressure, humidity float64, light, num int) {
	var cstSh, _ = time.LoadLocation("Asia/Shanghai")
	now := time.Now().In(cstSh).Format("2006-01-02 15:04:05")

	fileName := "box_log.csv"
	file, err := os.OpenFile(fileName, os.O_APPEND|os.O_RDWR, 0666)
	if err != nil {
		fmt.Println(fileName, "does not exist!\nerror:", err)
	}
	w := csv.NewWriter(file)
	// file.WriteString("\xEF\xBB\xBF")
	defer file.Close()

	// w.Write([]string{"Time", "Tempreture","Pressure","Humidity","light"})
	w.Write([]string{strconv.Itoa(num), now, strconv.FormatFloat(tempreture, 'f', 3, 64), strconv.FormatFloat(pressure, 'f', 3, 64), strconv.FormatFloat(humidity, 'f', 3, 64), strconv.Itoa(light)})
	w.Flush()

}

func getLight() int {
	cmd := exec.Command("./tsl")
	output, _ := cmd.CombinedOutput()
	// fmt.Println(string(output))
	regLight := "Lux = [0-9]+"
	light := regexp.MustCompile(regLight).FindAllString(string(output), -1)[0]
	lightInt, _ := strconv.Atoi(string([]byte(light)[6:]))
	return lightInt
}

func getLightStable() int {
	lightInt1 := getLight()
	time.Sleep(time.Second)
	lightInt2 := getLight()
	time.Sleep(time.Second)
	lightInt3 := getLight()
	time.Sleep(time.Second)
	lightInt4 := getLight()
	time.Sleep(time.Second)
	lightInt5 := getLight()
	return (lightInt1 + lightInt2 + lightInt3 + lightInt4 + lightInt5) / 5

}

//getAir 返回温度、气压、湿度
func getAir() (float64, float64, float64) {
	cmd := exec.Command("./bme280")
	output, _ := cmd.CombinedOutput()
	// fmt.Println(string(output))
	regTempreture := "[0-9][0-9].[0-9][0-9]\\*C"
	regPressure := "[0-9][0-9][0-9].[0-9][0-9]hPa"
	regHumidity := "[0-9][0-9].[0-9][0-9]\\%"

	tempreture := regexp.MustCompile(regTempreture).FindAllString(string(output), -1)[0]
	// a := string([]byte(Tempreture)[:5])
	// fmt.Println(strconv.Atoi(a))
	tempretureFloat, _ := strconv.ParseFloat(string([]byte(tempreture)[:5]), 64)
	pressure := regexp.MustCompile(regPressure).FindAllString(string(output), -1)[0]
	pressureFloat, _ := strconv.ParseFloat(string([]byte(pressure)[:6]), 64)
	humidity := regexp.MustCompile(regHumidity).FindAllString(string(output), -1)[0]
	humidityFloat, _ := strconv.ParseFloat(string([]byte(humidity)[:5]), 64)
	return tempretureFloat, pressureFloat, humidityFloat

}

func getAirStable() (float64, float64, float64) {
	tempretureFloat1, pressureFloat1, humidityFloat1 := getAir()
	time.Sleep(time.Second)
	tempretureFloat2, pressureFloat2, humidityFloat2 := getAir()
	time.Sleep(time.Second)
	tempretureFloat3, pressureFloat3, humidityFloat3 := getAir()
	time.Sleep(time.Second)
	tempretureFloat4, pressureFloat4, humidityFloat4 := getAir()
	time.Sleep(time.Second)
	tempretureFloat5, pressureFloat5, humidityFloat5 := getAir()
	tempretureFloat := (tempretureFloat1 + tempretureFloat2 + tempretureFloat3 + tempretureFloat4 + tempretureFloat5) / 5
	pressureFloat := (pressureFloat1 + pressureFloat2 + pressureFloat3 + pressureFloat4 + pressureFloat5) / 5
	humidityFloat := (humidityFloat1 + humidityFloat2 + humidityFloat3 + humidityFloat4 + humidityFloat5) / 5
	return tempretureFloat, pressureFloat, humidityFloat

}
func setup(script string, config Config) {

	//启动LED
	ChangeMode(script, config.PinLED, "25", "LED")
	//启动风扇1
	ChangeMode(script, config.PinFAN1, "100", "FAN")
	//启动风扇2
	ChangeMode(script, config.PinFAN2, "100", "FAN")
	//启动舵机
	ChangeMode(script, config.PinSERVO, "0", "SERVO")
}

//ChangeMode 第一个参数为脚本路径及名称，后三个分别是setup或stop、引脚号、空占比
func ChangeMode(script, pin, fc, mode string) {
	cmd := exec.Command("python3", script, pin, fc, mode)
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Change mode error: ", err.Error())
	}
	fmt.Println(string(output))
}

type Config struct {
	PinLED         string `json:"pin_LED"`
	PinFAN1        string `json:"pin_FAN1"`
	PinFAN2        string `json:"pin_FAN2"`
	PinSERVO       string `json:"pin_SERVO"`
	Pi4BAddress    string `json:"pi_4b_address"`
	Pi4BBoxPort    string `json:"pi_4b_box_port"`
	Pi4BRouterPort string `json:"pi_4b_router_port"`
	PiZeroAddress  string `json:"pi_zero_address"`
	PiZeroPort     string `json:"pi_zero_port"`
}

func readConfig() Config {
	var config Config
	datas, err := os.Open("../config.json")
	defer datas.Close()
	if err != nil {
		fmt.Println("error:", err)
		return config
	}
	data, err := ioutil.ReadAll(datas)
	if err != nil {
		fmt.Println("error:", err)
		return config
	}
	fmt.Println(string(data))

	err = json.Unmarshal([]byte(data), &config)

	if err != nil {
		fmt.Println("error:", err)
		return config
	}
	return config
}
