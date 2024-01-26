#!/bin/bash
# comment
curl -sfL -w "\n%{http_code}" $1 | { read body; read code; if [ $code == 200 ]; then
echo $body
fi
}
