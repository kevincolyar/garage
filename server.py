import re
import threading
import time
from datetime import datetime
from flask import Flask, jsonify, abort
from hardware import Hardware

app = Flask(__name__)

hardware = Hardware({
  'garage.door.left.closed'  : {'type': 'input', 'pin': 25},
  'garage.door.right.closed' : {'type': 'input', 'pin': 23},
  'garage.temperature.f'     : {'type': 'temperature.f', 'pin': 4},
  'garage.temperature.c'     : {'type': 'temperature.c', 'pin': 4},
  'garage.humidity'          : {'type': 'humidity', 'pin': 4},
})

state = {}

def worker():
  global state
  global hardware

  while True:
    state = hardware.latest()
    time.sleep(10)

t = threading.Thread(target=worker)
t.start()

@app.route('/')
def main():
  global state
  resp = jsonify(state)
  resp.status_code = 200
  return resp

@app.route("/<path:path>", methods=['GET'])
def get(path):
  global state
  key = re.sub('/', '.', path)

  if key in state:
    resp = jsonify({key: state[key]})
    resp.status_code = 200
    return resp
  else:
    abort(404)

@app.route("/<path:path>", methods=['POST'])
def post(path):
  global state
  key = re.sub('/', '.', path)

  if key in state:
    resp = jsonify({key: state[key]})
    resp.status_code = 200
    return resp
  else:
    abort(404)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
