package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
	"text/template"
	"time"

	"github.com/gorilla/websocket"
)

type data struct {
	Time                  float64
	Pressure, Temperature string
}

var (
	upgrader = websocket.Upgrader{}
	channel  = make(chan data, 1000)
	start    = time.Now()
)

func get(w http.ResponseWriter, r *http.Request) {
	fmt.Println(formatRequest(r))
	pressure := r.PostFormValue("pressure")
	temperature := r.PostFormValue("temperature")
	fmt.Println(pressure, temperature)
	channel <- data{
		time.Now().Sub(start).Seconds(),
		pressure,
		temperature,
	}
}

func ws(w http.ResponseWriter, r *http.Request) {
	ws, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Fprintf(w, "Couldn't connect lol")
		return
	}
	for dat := range channel {
		if err := ws.WriteJSON(dat); err != nil {
			fmt.Fprintf(w, "Marshal error")
			return
		}
	}
}

func akshat(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("data.html")
	if err != nil {
		panic(err)
	}
	t.Execute(w, nil)
}

func main() {
	ip := os.Args[1]
	http.HandleFunc("/", akshat)
	http.HandleFunc("/get", get)
	http.HandleFunc("/ws", ws)
	http.ListenAndServe(ip+":8080", nil)
}

// formatRequest generates ascii representation of a request
func formatRequest(r *http.Request) string {
	// Create return string
	var request []string
	// Add the request string
	url := fmt.Sprintf("%v %v %v", r.Method, r.URL, r.Proto)
	request = append(request, url)
	// Add the host
	request = append(request, fmt.Sprintf("Host: %v", r.Host))
	// Loop through headers
	for name, headers := range r.Header {
		name = strings.ToLower(name)
		for _, h := range headers {
			request = append(request, fmt.Sprintf("%v: %v", name, h))
		}
	}

	// If this is a POST, add post data
	if r.Method == "POST" {
		r.ParseForm()
		request = append(request, "\n")
		request = append(request, r.Form.Encode())
	}
	// Return the request as a string
	return strings.Join(request, "\n")
}
