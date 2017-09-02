#!/bin/bash

echo "Starting server: http://0.0.0.0:8000/"
`chromium-browser --kiosk http://0.0.0.0:8000/index1.html`
python -m SimpleHTTPServer 8000
