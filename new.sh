#!/bin/bash

# 30분마다 git add, commit, push 수행
while true
do
    current_time=$(date +"%Y-%m-%d %H:%M")
    git add .
    git commit -m "$current_time"
    git push
    sleep 1800
done
