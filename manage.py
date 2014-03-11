"""
Manager for massroute web-based application using Flask
"""
from flask.ext.script import Manager
from massroute import app

manager = Manager(app)

if __name__ == '__main__':
  manager.run()
