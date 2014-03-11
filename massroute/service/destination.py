import requests
import settings

class Destination():

  def get(self, routeid, destinationid):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    req = requests.get(settings.BASE_URL + '/routes/' + \
      routeid + '/destinations/' + \
      destinationid, headers=headers)
    return req.json()
