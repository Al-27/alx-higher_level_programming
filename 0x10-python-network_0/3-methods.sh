#!/bin/bash
# comment
curl -sI $1 | grep "Allow:" | sed "s/allow: //i"
