import requests
import settings

class Routes():

  def get(self):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    req = requests.get(settings.BASE_URL + '/routes', headers=headers)
    return req.json()

class Route():

  def get(self, id):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    req = requests.get(settings.BASE_URL + '/routes/' + id, headers=headers)
    return req.json()