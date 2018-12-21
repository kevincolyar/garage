http://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

## Usage

### Service Status

    sudo systemctl status garage.service

### Stop Service

    sudo systemctl stop garage.service

### Service Log

    sudo journalctl -u garage.service -b

states/routes

'garage.door.left.open': 0
'garage.door.right.open': 0
'sprinkler.station.01.open': 0
'garage.temperature': 0

/doors/left
## TODOs

* [ ] Web server
* [ ] Routes
* [ ] State Machine
* [ ] Pi test script
* [ ] Start server at startup (systemd, cron?)
* [ ] Connect to Home Assistant
* [ ] Tempature sensor
	http://www.raspberrywebserver.com/gpio/connecting-a-temperature-sensor-to-gpio.html
