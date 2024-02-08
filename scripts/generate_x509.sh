#!/bin/bash

# if second argument is not provided, use the default
SUBJ="/C=US/ST=WA/L=Seattle/O=DiscordBot"

# create the primary cert directory
CERT_DIR=$(pwd)/tmp_certs

# Create a server dir to store the server certificates
SERVER_DIR=$(pwd)/db/certs

# create a bot dir to store the bot certificates
BOT_DIR=$(pwd)/bot/certs

# create a api dir to store the api certificates
API_DIR=$(pwd)/api/certs

# create a web dir to store the web certificates
WEB_DIR=$(pwd)/web/certs

# Function to display help message
display_help() {
    echo "Usage: generate_x509.sh [OPTION]"
    echo "Options:"
    echo "  help     Display this help message"
    echo "  generate Generate x509 certificates"
    echo "  delete   Delete x509 certificates"
}

# Function to generate x509 certificates
generate_certificates() {
    # Check if the directory exists, if not create it
    check_dir $CERT_DIR
    check_dir $SERVER_DIR
    check_dir $BOT_DIR
    check_dir $API_DIR
    check_dir $WEB_DIR

    # Generate the private key for the x509 CA
    openssl ecparam -name secp384r1 -genkey -out $CERT_DIR/ca.key

    # Generate the self-signed certificate x509 for the CA
    openssl req -new -x509 -key $CERT_DIR/ca.key -out $CERT_DIR/ca.crt -subj $SUBJ

    # Convert CA certificate to PEM format
    openssl x509 -in $CERT_DIR/ca.crt -out $CERT_DIR/ca.pem -days 365 -outform PEM

    # copy the ca cert and key to the server, bot, api and web directories
    copy $CERT_DIR/ca.pem $SERVER_DIR/ca.pem
    copy $CERT_DIR/ca.pem $BOT_DIR/ca.pem
    copy $CERT_DIR/ca.pem $API_DIR/ca.pem
    copy $CERT_DIR/ca.pem $WEB_DIR/ca.pem

    # Generate the client certificate for the server, bot, api and web
    generate_client_certificates mongo-db $SERVER_DIR
    generate_client_certificates bot $BOT_DIR
    generate_client_certificates api $API_DIR
    generate_client_certificates web $WEB_DIR
    
    # delete the $CERT_DIR
    rm -rf $CERT_DIR
}

generate_client_certificates() {
    # generate the client key 
    openssl ecparam -name secp384r1 -genkey -out $CERT_DIR/$1.key

    # generate the client certificate
    openssl req -new -key $CERT_DIR/$1.key -out $CERT_DIR/$1.csr -subj $SUBJ/CN=$1

    # sign the client certificate
    openssl x509 -req -in $CERT_DIR/$1.csr -CA $CERT_DIR/ca.crt -CAkey $CERT_DIR/ca.key -CAcreateserial -out $CERT_DIR/$1.crt -days 365 -sha256

    # combine the client key and certificate into a single pem file
    cat $CERT_DIR/$1.key $CERT_DIR/$1.crt > $2/$1.pem
}

check_dir() {
    if [ ! -d $1 ]; then
        mkdir -p $1
    else
        echo "Directory $1 already exists, run delete before generating certificates"
        exit 1
    fi
}

copy() {
    if [ ! -f $2 ]; then
        cp $1 $2
    fi
}

# Function to delete x509 certificates
delete_certificates() {

    # Check if the directory exists, if it does delete it
    if [ -d $CERT_DIR ]; then
        rm -rf $CERT_DIR        
        echo "Cert directory deleted"
    fi

    if [ -d $SERVER_DIR ]; then
        rm -rf $SERVER_DIR
        echo "Server cert directory deleted"
    fi

    if [ -d $BOT_DIR ]; then
        rm -rf $BOT_DIR
        echo "Bot cert directory deleted"
    fi

    if [ -d $API_DIR ]; then
        rm -rf $API_DIR
        echo "api cert directory deleted"
    fi

    if [ -d $WEB_DIR ]; then
        rm -rf $WEB_DIR
        echo "web cert directory deleted"
    fi
    
    # Advise the user that certificates have been deleted
    echo "Certificates have been deleted"
}

# Check the command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            display_help
            exit 0
            ;;
        -g|--generate)
            generate_certificates
            exit 0
            ;;
        -d|--delete)
            delete_certificates
            exit 0
            ;;
        *)
            echo "Invalid option: $1"
            display_help
            exit 1
            ;;
    esac
    shift
done

# If no flag is provided, check if the dirs exists. If they do delete them and generate new certs
if [ -d $CERT_DIR ] || [ -d $SERVER_DIR ] || [ -d $BOT_DIR ] || [ -d $API_DIR ] || [ -d $WEB_DIR ]; then
    delete_certificates
fi
generate_certificates








