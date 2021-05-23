# SIMCom development platform for [PlatformIO](http://platformio.org)
[![version](https://img.shields.io/badge/version-0.0.1-brightgreen.svg)](CHANGELOG.md)
[![GitHub issues](https://img.shields.io/github/issues/umeshwalkar/platform-simcom.svg)](https://github.com/umeshwalkar/platform-simcom/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/umeshwalkar/platform-simcom.svg)](https://github.com/umeshwalkar/platform-simcom/pulls)
[![codacy](https://img.shields.io/codacy/grade/4ccbea0317c4415eb2d1c562feced407/master.svg)](https://app.codacy.com/manual/umeshwalkar/platform-simcom/dashboard)

**A few words in the beginning**
* **Version: 0.0.1** ( [look here, if there is something new](https://github.com/umeshwalkar/platform-simcom/wiki/FIX) )
* This project is not an official product of SIMCom and is based on **reverse engineering**.
* It is in the initial level of development. I am not a python programmer so any one who has better idea for creating workspace are welcome.
* Frameworks: 
* * EmbeddedAT ( SIM868 ) 
* **Windows**, Linux, macOS ( test and report )
* Read [WIKI](https://github.com/umeshwalkar/platform-simcom/wiki/PLATFORM-SIMCOM)
* [Examples](https://github.com/umeshwalkar/platformio-simcom-examples) 

**it should look like this...**

![Project](https://raw.githubusercontent.com/umeshwalkar/LIB/master/simcom/platform.png) 

## Install Platform

_Python 2 & 3 compatable in process, if issue - report_

**Method-1** (not uploaded in platformio bintray, so may get installation error)
* PIO Home > Platforms > Advanced Installation 
* paste https://github.com/umeshwalkar/platform-simcom

**Method-2** (suggested for now)
* Open PlatformIO powershell terminal 
* run command, **pio platform install https://github.com/umeshwalkar/platform-simcom.git**

**How to: [WIKI](https://github.com/umeshwalkar/platform-simcom/wiki/PLATFORM-SIMCOM)**
 and [EXAMPLES](https://github.com/umeshwalkar/platformio-simcom-examples)

## Fast Uninstall
* goto C:\Users\USER_NAME.platformio\platforms 
* delete folder **simcom** ( builders )
* delete folder **framework-simcom** ( sources )
* delete folder tool-simcom ( any tools, _may not delete_ )
* delete folder toolchain-armcc-simcom (compiler, _may not delete_ )

## Thanks to

* [Georgi Angelov](https://github.com/Wiz-IO)
* He is the inspiration to me for this particular work. I tried to learn from his work and trying to give it back to open source community.

**Support links**

* [Forum PlatformIO](https://community.platformio.org)


>If you want to help / support:   
[![donate](https://img.shields.io/badge/donate-PayPal-blue.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8HEWFU6AKMTXL&lc=US&no_note=0&currency_code=INR)


