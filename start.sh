#/usr/bin/env bash

set -e

#worker_class from 'sync' to 'gevent'
                    
# https://stackoverflow.com/questions/35837786/how-to-run-flask-with-gunicorn-in-multithreaded-mode

#sudo \
gunicorn server:app \
  -b 0.0.0.0:8080 \
  -k gevent \
  --log-level=DEBUG
#  --worker-connections 1000 \
