from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

admin = Admin(app, name='Portfolio', template_mode='bootstrap3')


from app import routes, models
from app.models import User, Roles
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Roles, db.session))

