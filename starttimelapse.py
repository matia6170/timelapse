import os
import datetime
import sys
import time
import subprocess
from time import sleep

# read the absolute path
#script_dir = os.path.dirname(__file__)
# call the .sh to capture the image


while True:
    currentsecond = datetime.datetime.now().strftime("%S")
    print currentsecond
    if currentsecond == '00' or currentsecond == '30' :
        os.system('DATE=$(date +"%Y-%m-%d_%H%M")')
        currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        test = '\''

        print 'saving'
        os.system('fswebcam -r 1280x720 --no-banner /home/pi/webcam/'+currentdate+'.jpg')
        print 'copying to usb'

        os.system('cp /home/pi/webcam/'+currentdate+'.jpg /media/pi/92ED-2DFE/webcam/\''+currentdate+'.jpg\'')

    sleep(0.5)


#get the date and time, set the date and time as a filename.
#currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# create the real path
#rel_path = currentdate +".jpg"
#  join the absolute path and created file name
#abs_file_path = os.path.join(script_dir, rel_path)
#print abs_file_path