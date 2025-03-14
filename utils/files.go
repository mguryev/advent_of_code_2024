package utils

import (
	"bufio"
	"io"
	"log"
	"os"
)

func ReadFile(path string) []string {
	file, err := os.Open(path)
	defer file.Close()

	if err != nil {
		log.Fatal(err)
	}

	reader := bufio.NewReader(file)
	var output []string = []string{}

	for true {
		line, err := reader.ReadString('\n')
		if err == io.EOF {
			break
		} else if err != nil {
			log.Println(err)
			break
		}

		output = append(output, line)
	}
	return output
}
