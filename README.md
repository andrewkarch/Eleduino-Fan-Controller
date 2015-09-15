# Eleduino Fan Controller for Raspberry Pi 2

A simple python script to control the fan of the [Eleduino 2015 New Version Raspberry Pi 2 mode B Transparent Acrylic Case With Fan](http://www.amazon.com/Eleduino-Version-Raspberry-Transparent-Acrylic/dp/B00ZEQ1PBI/)

Once the case is assembled [connect the black wire to pin 6 and red pin to 8](http://i.imgur.com/XryHosU.jpg)

Boot the Raspberry Pi

Download the script

> git clone https://github.com/andrewkarch/Eleduino-Fan-Controller.git

Open your rc.local file

> sudo nano /etc/rc.local

Add this line to your /etc/rc.local If you didn't change the working directory (cd) when downloading the script, the directory will be  be /home/pi/Eleduino-Fan-Controller

> sudo python /directory/to/fanController.py &

Reboot and the fan will now turn on if the temperature gets above 45C. To change the temperature open the script in leafpad, and change maxTemp to the temperature you want the fan to turn on at in Celcius.