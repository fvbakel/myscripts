#!/bin/sh
echo Sending $1
echo sudo gpsbabel -t -i gpx -f $1 -o garmin -F usb:
sudo gpsbabel -t -i gpx -f $1 -o garmin -F usb:
if [ $? -eq 0 ]
then
   echo "Copy is done"
else
   echo "Copy failed"
   read -p "Press enter to continue"
fi