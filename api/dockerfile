FROM golang:latest

# Set the Current Working Directory inside the container
WORKDIR /build

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# build the binary
RUN go build -o build/api

# copy the binary to the final container
COPY build/api /app/api

# set the live working directory
WORKDIR /app

# Expose port 8080 to the outside world
EXPOSE 8443

# Command to run the executable
CMD ["./api"]