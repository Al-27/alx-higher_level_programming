#!/bin/bash
# comment
curl -s --data @$2 --header "Content-Type: application/json" $1
