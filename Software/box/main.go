package main

import (
	"fmt"
	"os/exec"
	"regexp"
	"strconv"
	"time"
)

func main() {
	scriptPwm := "./pwm_control.py"
	setup(scriptPwm)
	tempreture, pressure, humidity := getAir()
	light := getLight()

	for {
		tempreture, pressure, humidity = getAir()
		light = getLight()

		//code here
		//根据气压、温度、湿度决定两个风扇的风速
		//监控内部亮度，改变亮度

		//此处记录各传感器数值
		fmt.Println("Tempreture:", tempreture)
		fmt.Println("Pressure:", pressure)
		fmt.Println("Humidity:", humidity)
		fmt.Println("Light:", light)
		time.Sleep(time.Second * 60)
	}
}
func getLight() int {
	cmd := exec.Command("./tsl")
	output, _ := cmd.CombinedOutput()
	// fmt.Println(string(output))
	regLight := "Visible light: [0-9]+"
	light := regexp.MustCompile(regLight).FindAllString(string(output), -1)[0]
	lightInt, _ := strconv.Atoi(string([]byte(light)[15:]))
	return lightInt
}

//getAir 返回温度、气压、湿度
func getAir() (float64, float64, float64) {
	cmd := exec.Command("./bme280")
	output, _ := cmd.CombinedOutput()
	// fmt.Println(string(output))
	regTempreture := "[0-9][0-9].[0-9][0-9]\\*C"
	regPressure := "[0-9][0-9][0-9].[0-9][0-9]hPa"
	regHumidity := "[0-9][0-9].[0-9][0-9]\\%"

	Tempreture := regexp.MustCompile(regTempreture).FindAllString(string(output), -1)[0]
	// a := string([]byte(Tempreture)[:5])
	// fmt.Println(strconv.Atoi(a))
	TempretureInt, _ := strconv.ParseFloat(string([]byte(Tempreture)[:5]), 64)
	Pressure := regexp.MustCompile(regPressure).FindAllString(string(output), -1)[0]
	PressureInt, _ := strconv.ParseFloat(string([]byte(Pressure)[:6]), 64)
	Humidity := regexp.MustCompile(regHumidity).FindAllString(string(output), -1)[0]
	HumidityInt, _ := strconv.ParseFloat(string([]byte(Humidity)[:5]), 64)
	return TempretureInt, PressureInt, HumidityInt

}
func setup(script string) {
	mode := "setup"
	pinLED := "32"
	pinFAN1 := "16"
	pinFAN2 := "22"
	pinRUD := "0"
	// fc:="50"
	//启动LED
	ChangeMode(script, mode, pinLED, "10")
	//启动风扇1
	ChangeMode(script, mode, pinFAN1, "10")
	//启动风扇2
	ChangeMode(script, mode, pinFAN2, "10")
	//启动舵机
	ChangeMode(script, mode, pinRUD, "0")
}

//ChangeMode 第一个参数为脚本路径及名称，后三个分别是setup或stop、引脚号、空占比
func ChangeMode(script, mode, pin, fc string) {
	cmd := exec.Command("python3", script, mode, pin, fc)
	_, err := cmd.Output()
	if err != nil {
		fmt.Println("error: ", err.Error())
	}
}
