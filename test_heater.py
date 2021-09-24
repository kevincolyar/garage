#!/usr/bin/env python

import time
from hardware import Hardware

def drange(start, stop, step):
  r = start
  while r < stop:
    yield r
    r += step

hardware = Hardware({
    'heater': {'type': 'servo', 'pin': 17},
    })


while True:
    for i in drange(2, 12, .1):
        print(i)
        hardware.set('heater', i)
        time.sleep(.1)


time.sleep(3)
hardware.set('heater', 7.5) # 90
time.sleep(3)
hardware.set('heater', 2.5) # 0
time.sleep(3)
hardware.set('heater', 12.5) # 180

time.sleep(100)
