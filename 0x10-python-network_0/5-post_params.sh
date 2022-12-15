#!/bin/bash
# send POST request and Display body 
curl -s -X POST -d "test@gmail.com&subject=I will always be here for PLD" "$1"
