"""
This script runs the PersonalApp application using a development server.
"""

from os import environ
from PersonalApp import app

if __name__ == '__main__':
    app.run()
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)