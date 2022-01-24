import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lexa:123qwe@localhost/regcity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "12345qwertasdfgQWERTASDFG!@#$%"
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app)
from models import *
admin.add_view(ModelView(Regions, db.session))
admin.add_view(ModelView(Cities, db.session, endpoint="cities_"))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)