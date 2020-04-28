#!/bin/bash

python3 parser.py
echo "" > links.txt
python3 zippyshare.py --in-file input.txt
wget -nc -i links.txt