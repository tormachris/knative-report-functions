package main

import (
  "fmt"
  "log"
  "net/http"
  "os"
)

func handler(w http.ResponseWriter, r *http.Request) {
    target := os.Getenv("TARGET")
    num, err := strconv.Atoi(target)
	if err != nil {
		return "", fmt.Errorf("Failed to parse %s as int! %v", target, err)
	}
	logrus.Infof("Checking if %s is prime", target)
	if num <= 1 {
		return fmt.Fprintf(w,"%d is not prime", num), nil
	}
	for i := 2; i <= int(math.Floor(float64(num)/2)); i++ {
		if num%i == 0 {
			return fmt.Fprintf(w,"%d is not prime", num), nil
		}
	}
	return fmt.Fprintf(w,"%d is prime", num), nil
}

func main() {
  log.Print("Hello world sample started.")

  http.HandleFunc("/", handler)

  port := os.Getenv("PORT")
  if port == "" {
    port = "8080"
  }

  log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
}
