package main
import (
	"net/http"
	"io"
    "os"
    "fmt"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello world!")
}


func main() {
    port := 8002
    fmt.Println("Listening on port ", port )
	http.HandleFunc("/simple/", helloHandler)
	http.ListenAndServe(port, nil)
}
