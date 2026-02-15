#!/bin/bash
service=$1
action=$2

function check_service(){
    local svc=$1
    # 2>&1 redirects 'Standard Error' to 'Standard Output' so we can capture it
    sudo systemctl status $svc 2>&1 
}

status=$(check_service $service)

# We use double brackets [[ ]] for string matching in Bash
# We check if the captured text contains "could not be found"
if [[ "$status" == *"could not be found"* && "$action" == "install"  ]]
then
    echo "Service $service not found. Installing..."
    sudo apt-get update
    sudo apt-get install $service -y
else
    echo "Service $service is already installed."
fi
