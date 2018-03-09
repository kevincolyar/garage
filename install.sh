#!/usr/bin/env bash

set -e

sudo cp ./garage.service /lib/systemd/system/
sudo systemctl enable garage.service
sudo systemctl start garage.service
