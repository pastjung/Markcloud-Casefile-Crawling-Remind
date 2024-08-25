#!/bin/sh
if [ ! -d ./venv/ ]; then \
    echo "[INFO] >> Installing dependencies, please wait..." && \
    python -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt && \
    pip freeze > requirements.txt && \
    python3 service/main.py \
;else \
    echo "[INFO] >> Ready to luanch server, checking new dependencies, please wait..." && \
    . venv/bin/activate && \
    pip install -r requirements.txt && \
    pip freeze > requirements.txt && \
    python3 service/main.py \
;fi