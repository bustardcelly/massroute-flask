"""
Massroute application for displaying rela-time bus traffic data on MBTA.
"""
from flask import Flask
from massroute.api import api

app = Flask('massroute')
app.register_blueprint(api, url_prefix='')
