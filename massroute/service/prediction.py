import requests
import settings

class Prediction():

  def get(self, routeid, destinationid, stopid):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    req = requests.get(settings.BASE_URL + \
      '/routes/' + routeid + \
      '/destinations/' + destinationid + \
      '/stops/' + stopid, headers=headers)
    return req.json()
