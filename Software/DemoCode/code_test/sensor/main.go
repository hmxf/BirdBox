package main

import (
	"fmt"
	"os/exec"
)

func main() {
	cmd := exec.Command("./bme280")
	output, _ := cmd.CombinedOutput()
	fmt.Println(string(output))
}
