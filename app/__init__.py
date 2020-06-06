from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db = SQLAlchemy(app)

# Initialize migration engine
migrate = Migrate(app, db)

login = LoginManager(app)
# Identify view function that handles logins
login.login_view = 'login'

from app import routes, models