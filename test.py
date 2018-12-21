import time
from hardware import Hardware

hardware = Hardware({
  'sprinkler.station.1': {'type': 'output', 'pin': 22},
  'sprinkler.station.2': {'type': 'output', 'pin': 27},
  'sprinkler.station.3': {'type': 'output', 'pin': 18},
  'sprinkler.station.4': {'type': 'output', 'pin': 17},
  'sprinkler.station.5': {'type': 'output', 'pin': 15},
  'sprinkler.station.6': {'type': 'output', 'pin': 14},
  'sprinkler.station.7': {'type': 'output', 'pin': 4},
  'sprinkler.station.8': {'type': 'output', 'pin': 3},
})


while True:
    for i in range(1, 9):
        hardware.set('sprinkler.station.' + str(i), True)
        time.sleep(.01)
        hardware.set('sprinkler.station.' + str(i), False)
        time.sleep(.01)
