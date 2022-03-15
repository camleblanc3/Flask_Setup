#import everything needed here
from flask import Flask 

#from config file you can import the config file
from config import Config

#import for database stuff
from .models import db
from flask_migrate import Migrate

#define Flask object
app = Flask(__name__, static_url_path = '/static', static_folder ='static')


#tell app how it should be configured -- on config.py file
app.config.from_object(Config)

#set up ORM and migrate connection
db.init_app(app)
migrate = Migrate(app, db)



from . import routes
from . import models