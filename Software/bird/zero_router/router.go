package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"os"
	"syscall"
)

var pid *os.Process

func main() {
	fmt.Println("hello world!")
	r := gin.Default()

	r.GET("/display", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "open the test",
		})
		if pid != nil {
			pid.Kill()
		}
		env := os.Environ()
		procAttr := &os.ProcAttr{
			Env: env,
			Files: []*os.File{
				os.Stdin,
				os.Stdout,
				os.Stderr,
			},
		}
		var err error
		//4b上测试
		//pid, err = os.StartProcess("/home/pi/BirdBox/Software/bird/zero_router/display.py", []string{""}, procAttr)
		//zero上测试
		pid, err = os.StartProcess("./base.py", []string{"3"}, procAttr)
		// pid, err = os.StartProcess("/home/pi/router/text/base.py", []string{"3"}, procAttr)
		fmt.Printf("Error %v starting process!", err) //
		os.Exit(1)
	})
	r.GET("close", func(c *gin.Context) {
		fmt.Println(pid)
		if pid != nil {
			// pid.Release()
			pid.Signal(syscall.SIGINT)
		}
	})
	r.GET("print", func(c *gin.Context) {
		fmt.Println(pid)
	})
	// r.GET("list", func(c *gin.Context) {
	r.POST("script", func(c *gin.Context) {
		scriptName := c.PostForm("script_name")
		sleepTime := c.PostForm("sleep_time")
		if pid != nil {
			pid.Kill()
		}
		env := os.Environ()
		procAttr := &os.ProcAttr{
			Env: env,
			Files: []*os.File{
				os.Stdin,
				os.Stdout,
				os.Stderr,
			},
		}
		var err error
		//4b上测试
		//pid, err = os.StartProcess("/home/pi/BirdBox/Software/bird/zero_router/display.py", []string{""}, procAttr)
		//zero上测试
		pid, err = os.StartProcess("./"+scriptName, []string{sleepTime}, procAttr)
		// pid, err = os.StartProcess("/home/pi/router/text/base.py", []string{"3"}, procAttr)
		fmt.Printf("Error %v starting process!", err) //
		fmt.Println(pid)

	})
	// })
	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}
