#!/usr/bin/env python

import time
import pigpio
import datetime

pi = pigpio.pi()
date = datetime.datetime.now()

sem = 0

try:
	while True:
		if date.hour >= 10 and date.hour < 18:
			if sem == 0:
				pi.set_servo_pulsewidth(18, 800) # 0 deg
				time.sleep(2)
				# pi.set_servo_pulsewidth(18, 1600) # 90 deg
				# time.sleep(2)
				# pi.set_servo_pulsewidth(18, 2400) # 180 deg
				# time.sleep(2)
				
			sem = 1
		else:
			pi.set_servo_pulsewidth(18, 1600) # 90 deg
			time.sleep(2)
			
except KeyboardInterrupt:
	pi.set_servo_pulsewidth(18, 2400) # 180 deg
	time.sleep(2)
	pi.set_servo_pulsewidth(18, 0) #turn servo off
	pi.stop()

