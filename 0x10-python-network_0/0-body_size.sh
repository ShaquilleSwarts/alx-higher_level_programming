#!/bin/bash
# Get the byte size of body
curl -s "$1" | wc -c
