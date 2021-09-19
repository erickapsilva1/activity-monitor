#!/bin/bash

export DISPLAY=:0.0
dir=/home/erick/apps/ss/

wname=$(xdotool getactivewindow getwindowname | sed -e "s/'/''/g")
echo "insert into LOG (\`WINDOW\`,\`USER\`) values ('$wname','$(whoami)');" | mysql --defaults-file=/home/erick/monitor.auth

mkdir -p $dir$(date +%Y-%m-%d)
import -window root -silent $dir$(date +%Y-%m-%d/)$(date +%Y-%m-%d-%H.%M.%S.jpg)

