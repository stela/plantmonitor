# Raspberry Pi plant humidity monitor

This is a rather quick-and dirty implementation of a plant humidity monitor for the raspberry Pi.
[plantmonitor.py](plantmonitor.py) is  the main file. grove_oled.py and grovepi.py
are libraries to access humidity, light and temperature sensors, and use
the small OLED display and LED to indicate status (see <https://github.com/DexterInd/GrovePi>).

To run this software you need a Rasberry PI (tested with model B), a Dexter Industries grovepi shield,
plus the sensors, LED and OLED display of course. 

Beware that the current implementation will corrode the humidity sensor within a few weeks to a few months,
by rewiring the sensor and adopting this software to only briefly pass current while measuring,
it should last much longer.

When using the latest raspbian distribution as of February 2019, in order to make it communicate with the i2c-based Dexter grovepi shield, add this line to `/boot/config.txt`:
```
dtoverlay=i2c1-bcm2708,combine=off
```
and reboot. This makes it use an older i2c driver which supports disabling transaction combining, which some devices have trouble with. See also <https://github.com/raspberrypi/firmware/issues/828>.
