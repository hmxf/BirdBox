package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"os"
	// "strconv"
	// "time"
)

func main() {

	fileName := "box_log.csv"
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
			fmt.Printf("can not read, err is %+v\n", err)
		}
		if err == io.EOF {
			break
		}
		row2 = row1
	}

	fmt.Println(row2[0])
}
