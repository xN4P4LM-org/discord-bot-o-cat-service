package main

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func get_server_cert() (string, string) {

	// get root path from env
	cert_path := os.Getenv("LETS_ENCRYPT_PATH")

	cert, cert_err := os.ReadFile(cert_path + "/fullchain.pem")
	key, key_err := os.ReadFile(cert_path + "/privkey.pem")

	if cert_err != nil || key_err != nil {
		os.Exit(-3)
	}

	return string(cert), string(key)
}

func main() {
	// get server cert for tls
	cert, key := get_server_cert()

	// create gin server
	r := gin.Default()

	// create ping route
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})

	// run server
	r.RunTLS("127.0.0.1:8443", cert, key)
}
