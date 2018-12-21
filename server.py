import re
import threading
import time
import json
from datetime import datetime
from flask import Flask, jsonify, abort, request, Response
from hardware import Hardware

app = Flask(__name__)

hardware = Hardware({
  'garage.door.left.closed'  : {'type': 'bool', 'pin': 25},
  'garage.door.right.closed' : {'type': 'bool', 'pin': 23},
  'garage.temperature.f'     : {'type': 'temperature.f', 'pin': 4},
  'garage.temperature.c'     : {'type': 'temperature.c', 'pin': 4},
  'garage.humidity'          : {'type': 'humidity', 'pin': 4},
  'sprinkler.station.1.on'   : {'type': 'bool', 'pin': 22},
  'sprinkler.station.2.on'   : {'type': 'bool', 'pin': 27},
  'sprinkler.station.3.on'   : {'type': 'bool', 'pin': 18},
  'sprinkler.station.4.on'   : {'type': 'bool', 'pin': 17},
  'sprinkler.station.5.on'   : {'type': 'bool', 'pin': 15},
  'sprinkler.station.6.on'   : {'type': 'bool', 'pin': 14},
  'sprinkler.station.7.on'   : {'type': 'bool', 'pin': 4},
  'sprinkler.station.8.on'   : {'type': 'bool', 'pin': 3},
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
    #state[key] = hardware.get(key)
    resp = Response(json.dumps(state[key]), mimetype=u'application/json')
    return resp
  else:
    abort(404)

@app.route("/<path:path>", methods=['POST'])
def post(path):
  global state
  key = re.sub('/', '.', path)
  value = True if request.get_data() == 'true' else False

  state[key] = value
  hardware.set(key, value)

  #resp = jsonify({key: value})
  resp = Response(json.dumps(value), mimetype=u'application/json')
  return resp

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
