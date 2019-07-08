#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://www.kiosko.es

while true; do
   xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
   sleep 10
done