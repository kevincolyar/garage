import RPi.GPIO as GPIO
import Adafruit_DHT
from functools import partial

class Hardware():
  def __init__(self, hw):
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    self.hw = hw

    for k,v in self.hw.items():
      if v['type'] == 'input':
        GPIO.setup(v['pin'], GPIO.IN)
        v['get'] = partial(GPIO.input, v['pin'])
      elif v['type'] == 'output':
        GPIO.setup(v['pin'], GPIO.OUT)
        #GPIO.output(v['pin'], GPIO.LOW)
        v['get'] = lambda: None
      elif v['type'] == 'temperature.f':
	  v['get'] = partial(self.read_temperature_f, v['pin'])
      elif v['type'] == 'temperature.c':
	  v['get'] = partial(self.read_temperature_c, v['pin'])
      elif v['type'] == 'humidity':
	  v['get'] = partial(self.read_humidity, v['pin'])
      else:
        raise(v['type'])

  def read_humidity(self, pin):
    v, _ = Adafruit_DHT.read(Adafruit_DHT.AM2302, pin)
    return v

  def read_temperature_c(self, pin):
    _, v = Adafruit_DHT.read(Adafruit_DHT.AM2302, pin)
    return v

  def read_temperature_f(self, pin):
    v = self.read_temperature_c(pin)
    if v:
      return v * (9./5.) + 32.
    return v

  def latest(self):
    return { k: v['get']() for k,v in self.hw.items() } 

  def get(self, k):
    return self.hw[k]['get']()

