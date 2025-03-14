package solutions

import (
	"log"
	"mguryev/advent_of_code2024/utils"
)

func Day1(dataFile string) {
	data := utils.ReadFile("data/" + dataFile)
	log.Println(len(data))
}
