#!/bin/bash

echo "Installing required tools..."

sudo apt update

sudo apt install python3 python3-pip git -y

go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

pip install sublist3r

echo "Updating nuclei templates..."

nuclei -update-templates

echo "Setup Completed!"