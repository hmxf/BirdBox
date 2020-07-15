package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"os"
	// "strings"
	// "os/exec"
	"io"
	"io/ioutil"
	"net/http"
	URL "net/url"
	"time"
)

func main() {
	config := readConfig()
	r := gin.Default()
	r.LoadHTMLFiles("views/index.html")
	r.StaticFS("/index", http.Dir("./views"))
	r.StaticFile("/log.csv", "../log/log.csv")
	r.StaticFile("/state.csv", "../../box/box_log.csv")
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.GET("/index", func(c *gin.Context) {
		c.HTML(200, "index.html", gin.H{})
	})
	r.GET("/print", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/print"
		url := config.PiZeroAddress + config.PiZeroPort + "/print"
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		fmt.Printf("response:%x\n", &response.Body)
		c.JSON(response.StatusCode, response.Body)
	})
	r.GET("/list", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/print"
		url := config.PiZeroAddress + config.PiZeroPort + "/list"
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		body, err := ioutil.ReadAll(response.Body)
		if err != nil {
			fmt.Println("error:", err)
		}
		fmt.Println(string(body))
		var a []FileMessage
		json.Unmarshal(body, &a)
		fmt.Println(a)
		c.JSON(response.StatusCode, a)
	})
	r.GET("/display", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/display"
		url := config.PiZeroAddress + config.PiZeroPort + "/display"
		fmt.Println(url)
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		fmt.Printf("response:%x\n", &response.Body)
		c.JSON(response.StatusCode, response.Body)
	})
	r.GET("/punish", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/display"
		url := "http://localhost:8081/punish"
		fmt.Println(url)
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		fmt.Printf("response:%x\n", &response.Body)
		c.JSON(response.StatusCode, response.Body)
	})
	r.GET("/unpunish", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/display"
		url := "http://localhost:8081/unpunish"
		fmt.Println(url)
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		fmt.Printf("response:%x\n", &response.Body)
		c.JSON(response.StatusCode, response.Body)
	})
	r.GET("/close", func(c *gin.Context) {

		client := &http.Client{}
		// url := "http://192.168.0.155:8080/close"
		url := config.PiZeroAddress + config.PiZeroPort + "/close"
		request, err := http.NewRequest("GET", url, nil)
		if err != nil {
			fmt.Println("error:", err)
		}
		response, err := client.Do(request)
		if err != nil {
			fmt.Println("error:", err)
		}
		defer response.Body.Close()
		fmt.Printf("response:%x\n", &response.Body)
		c.JSON(response.StatusCode, response.Body)
	})
	r.GET("/message", func(c *gin.Context) {
		message := getLine("../../box/box_log.csv")
		c.JSON(200, gin.H{
			"Tempreture": message[2],
			"Humidity":   message[4],
			"Light":      message[5],
			"Pressure":   message[3],
		})
	})
	r.POST("/bird", index())
	r.POST("/script", func(c *gin.Context) {

		url := config.PiZeroAddress + config.PiZeroPort + "/script"
		fmt.Println(url)

		data := make(URL.Values)

		scriptName := c.PostFormArray("script_name")
		sleepTime := c.PostFormArray("sleep_time")
		fmt.Println("name:", scriptName)
		fmt.Println("time:", sleepTime)
		data["script_name"] = scriptName
		data["sleep_time"] = sleepTime
		res, err := http.PostForm(url, data)
		fmt.Println(data)
		if err != nil {
			fmt.Println("error:", err.Error())
			return
		}
		defer res.Body.Close()
		fmt.Printf("response:%x\n", &res.Body)
		c.JSON(res.StatusCode, res.Body)
	})
	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}

func log(c *gin.Context) {
	var cstSh, _ = time.LoadLocation("Asia/Shanghai")
	fmt.Println(time.Now().In(cstSh).Format("2006-01-02 15:04:05"))
	date := time.Now().In(cstSh).Format("20060102")
	file, _ := os.OpenFile("../log/log.csv", os.O_APPEND|os.O_RDWR, 0666)
	w := csv.NewWriter(file)
	// file.WriteString("\xEF\xBB\xBF")
	defer file.Close()
	time := c.PostForm("time")
	action := c.PostForm("action")
	x := c.PostForm("x")
	y := c.PostForm("y")
	fmt.Println(time)
	fmt.Println(action)
	fmt.Println(x, y)
	w.Write([]string{date, time, action, "(" + x + "," + y + ")"})
	w.Flush()
}

func index() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "got it",
		})
		log(c)
	}
}

func getLine(fileName string) []string {

	fs, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("can not open the file, err is %+v", err)
		return []string{}
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
			break
		}
		if err == io.EOF {
			break
		}
		row2 = row1
	}
	return row2
}

//Config 读取配置文件的结构体
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
	datas, err := os.Open("../../config.json")
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

//FileMessage 文件信息结构体
type FileMessage struct {
	Name string `json:"name"`
	Time string `json:"time"`
}
