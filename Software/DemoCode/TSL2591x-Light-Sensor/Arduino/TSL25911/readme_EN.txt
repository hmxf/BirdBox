/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-09-24
* | Info        :   Here is a Chinese version of the documentation for your quick use.
******************************************************************************/
This file is to help you use this routine.

1.Basic Information：
This routine was developed based on Arduino, and the routines were verified on the Arduino UNO.
This routine was verified using the TSL2591x_Light_Sensor.

2.Pin connection：
Pin connections can be viewed in DEV_Config.h and will be repeated here:
e-Paper Shield   =>    Arduino
VCC              =>    3.3V/5V
GND              =>    GND
SCL              ->    SCL
SDA              ->    SDA
INT              ->    8



3.Basic use：
Since this project is a comprehensive project, you may need to read the following for use:
method 1:
    Copy the entire EPD folder to the libraries folder under the Arduino installation path.
        ..\Arduino\libraries
Method 2:
    Copy the src folder in the EPD folder to
        C:\Users\user_name\Documents\Arduino\libraries
        or ..\document\Arduino\libraries

Then open the corresponding project burn in the examples folder.
