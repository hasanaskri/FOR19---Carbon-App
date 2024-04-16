
from flask import Flask
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
    return "<h1>Home page</h1>" \
        "<p>In this project we develop and app...</p>"

@application.route('/developers')
def developers():
    return "<h1>Developers</h1>" \
        "<p>In this webpage, we introduce the developers of the app...</p>"

@application.route('/app_calculator')
def app_calculator():
    return "<h1>App Calculator</h1>" \
        "<p>In this webpage, we develop an app to work out transport carbon emissions...</p>"

if __name__ == '_main_':
    application.run(debug=True)
