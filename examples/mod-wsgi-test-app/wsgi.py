from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello():
    return b'Hello World from mod_wsgi hosted WSGI application! test insatll other package ~~  '

if __name__ == '__main__':
    application.run()
