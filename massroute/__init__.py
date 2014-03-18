"""
Massroute application for displaying rela-time bus traffic data on MBTA.
"""
from flask import Flask
from massroute.api import api

app = Flask('massroute')
app.register_blueprint(api, url_prefix='')

def predictions_list(predictions):
  return isinstance(predictions, list)
  
def format_prediction(minutes, seconds):
  return minutes + ' minutes ' + str(int(seconds) % 60) + ' seconds' if int(minutes) > 0 else seconds + ' seconds'

def format_prediction_breadcrumb(prediction):
  breadcrumb = '/routes/' + prediction["routeTag"]
  dir_tag = None if len(prediction["predictions"]) == 0 else prediction["predictions"][0]["dirTag"]
  return breadcrumb if dir_tag == None else '%s/destinations/%s' % (breadcrumb, dir_tag)

app.jinja_env.globals.update(format_prediction_breadcrumb=format_prediction_breadcrumb)
app.jinja_env.globals.update(format_prediction=format_prediction)
app.jinja_env.globals.update(predictions_list=predictions_list)
