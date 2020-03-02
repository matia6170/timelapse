#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg

cp /home/pi/webcam/$DATE.jpg /media/pi/92ED-2DFE/webcam/$DATE