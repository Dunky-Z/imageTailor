#!/bin/bash

rsync -avz  -e "ssh -p 12066"  "root@localhost:/opt/imageTailor" "/home/user/develop/imageTailor/dev"
