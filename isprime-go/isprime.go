package main

import (
  "fmt"
  "log"
  "net/http"
  "os"
  "math"
  "strconv"
)

func handler(w http.ResponseWriter, r *http.Request) {
    target := os.Getenv("TARGET")
    num, err := strconv.Atoi(target)
	if err != nil {
		fmt.Errorf("Failed to parse %s as int! %v", target, err)
	}
	if num <= 1 {
		fmt.Sprintf("%d is not prime", num)
	}
	for i := 2; i <= int(math.Floor(float64(num)/2)); i++ {
		if num%i == 0 {
			fmt.Sprintf("%d is not prime", num)
		}
	}
	fmt.Sprintf("%d is prime", num)
}

func main() {
  http.HandleFunc("/", handler)

  port := os.Getenv("PORT")
  if port == "" {
    port = "8080"
  }

  log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}
