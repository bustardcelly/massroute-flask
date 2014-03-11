import sys, traceback
from flask import render_template
from flask import Blueprint

from massroute.service import routes, route
from massroute.service import destination

api = Blueprint('api', __name__)

@api.route('/')
def index():
  payload = {}
  try:
    payload = routes.get()
  except:
    traceback.print_exc()
    return 'Could not load Routes.'
  return render_template('index.html', routes=payload)

@api.route('/routes/<routeid>')
def get_route(routeid):
  payload = {}
  try:
    payload = route.get(routeid)
  except:
    traceback.print_exc()
    return 'Could not load Route with id %s.' % routeid
  return render_template('route.html', route=payload)

@api.route('/routes/<routeid>/destinations/<destinationid>')
def get_destination(routeid, destinationid):
  payload = {}
  try:
    payload = destination.get(routeid, destinationid)
  except:
    traceback.print_exc()
    return 'Could not load Destination data with id %s.' % destinationid
  print "%r" % str(payload)
  return render_template('destination.html', destination=payload)

@api.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404
