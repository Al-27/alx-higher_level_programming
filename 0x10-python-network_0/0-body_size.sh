#!/bin/bash
# comment
curl -sI $1 | grep "Content-L" | sed "s/content-length: //i"
