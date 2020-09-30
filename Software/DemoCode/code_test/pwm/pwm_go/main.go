package main

import (
	"fmt"
	"os/exec"
)

func main() {

}

func ChangeMode(script, mode, pin, fc string) {
	cmd := exec.Command("python3", script, mode, pin, fc)
	_, err := cmd.Output()
	if err != nil {
		fmt.Println("error: ", err.Error())
	}
}
