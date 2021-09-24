import RPi.GPIO as GPIO
import Adafruit_DHT
from functools import partial
import time

def bool_input(pin):
    return True if GPIO.input(pin) else False 
def bool_output(pin, val):
    return GPIO.output(pin, GPIO.HIGH if val else GPIO.LOW)

class Hardware():
  def __init__(self, hw):
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    self.hw = hw

    for k,v in self.hw.items():
      if v['type'] == 'bool':
        GPIO.setup(v['pin'], GPIO.OUT)
        v['get'] = partial(bool_input, v['pin'])
        v['set'] = partial(bool_output, v['pin'])
      elif v['type'] == 'temperature.f':
	  v['get'] = partial(self.read_temperature_f, v['pin'])
      elif v['type'] == 'temperature.c':
	  v['get'] = partial(self.read_temperature_c, v['pin'])
      elif v['type'] == 'humidity':
	  v['get'] = partial(self.read_humidity, v['pin'])
      elif v['type'] == 'servo':
          GPIO.setup(v['pin'], GPIO.OUT)
          pwm = GPIO.PWM(v['pin'], 50) # 50Hz
          pwm.start(0)
	  v['set'] = partial(self.set_servo, pwm, v['pin'])
          v['get'] = partial(GPIO.input, v['pin'])
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

  def set(self, k, v):
    self.hw[k]['set'](v)

  def set_servo(self, pwm, pin, v):
      GPIO.output(pin, True)
      pwm.ChangeDutyCycle(v)
      time.sleep(2)
      GPIO.output(pin, False)
      pwm.ChangeDutyCycle(0)

