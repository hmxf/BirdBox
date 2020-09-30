package main

import (
	"fmt"
	"os"
)

func main() {
	env := os.Environ()
	procAttr := &os.ProcAttr{
		Env: env,
		Files: []*os.File{
			os.Stdin,
			os.Stdout,
			os.Stderr,
		},
	}
	pid1, err := os.StartProcess("/home/pi/BirdBox/Software/box/main", []string{}, procAttr)
	pid2, err := os.StartProcess("/home/pi/BirdBox/Software/bird/router/test_router", []string{}, procAttr)
	pid3, err := os.StartProcess("/home/pi/BirdBox/Software/APP/bird-linux-armv7l/bird", []string{}, procAttr)
	fmt.Println(pid1, pid2, pid3, err)
}
