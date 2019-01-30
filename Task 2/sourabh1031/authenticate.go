package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
)

func main() {

	fmt.Println("Enter Username")
	var email, password string
	_, err := fmt.Scanf("%s", &email)
	if err != nil {
		panic(err)
	}

	fmt.Println("Enter Password")
	_, err1 := fmt.Scanf("%s", &password)
	if err1 != nil {
		panic(err1)
	}

	re := regexp.MustCompile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

	if re.MatchString(email) != true {
		log.Fatal("Incorrect email!! Please try again...")
		os.Exit(1)
	}
	if len(password) < 8 {
		log.Fatal("Password length is less than 8 characters")
	}
}
