package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("hello world!")
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.POST("/post_test", POSTTest)
	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}

func POSTTest(c *gin.Context) {
	x := c.PostForm("x")
	y := c.PostForm("y")
	userName := c.PostForm("username")
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(userName)
}
