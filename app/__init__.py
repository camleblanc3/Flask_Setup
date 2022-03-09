#import everything needed here
from flask import Flask 

#from config file you can import the config file
from config import Config

#define Flask object
app = Flask(__name__)

#tell app how it should be configured -- on config.py file
app.config.from_object(Config)


from . import routes