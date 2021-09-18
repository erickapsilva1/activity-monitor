#!/bin/bash

export DISPLAY=:0.0

wname=$(xdotool getactivewindow getwindowname | sed -e "s/'/''/g")
echo "insert into LOG (\`WINDOW\`,\`USER\`) values ('$wname','$(whoami)');" | mysql --defaults-file=/home/erick/monitor.auth

