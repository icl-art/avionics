package main

import (
	"fmt"
	"net/http"
	"strconv"
	"text/template"
	"time"

	"github.com/gorilla/websocket"
)

type data struct {
	Time, Pressure, Temperature float64
}

var (
	upgrader = websocket.Upgrader{}
	channel  = make(chan data, 10)
	start    = time.Now()
)

func recv(w http.ResponseWriter, r *http.Request) {
	pressure, err := strconv.ParseFloat(r.PostFormValue("pressure"), 64)
	if err != nil {
		panic(err)
	}
	temperature, err := strconv.ParseFloat(r.PostFormValue("temperature"), 64)
	if err != nil {
		panic(err)
	}
	channel <- data{
		time.Now().Sub(start).Seconds(),
		pressure,
		temperature,
	}
}

func get(w http.ResponseWriter, r *http.Request) {
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
	http.HandleFunc("/", akshat)
	http.HandleFunc("/get", recv)
	http.HandleFunc("/ws", get)
	http.ListenAndServe(":8080", nil)
}
