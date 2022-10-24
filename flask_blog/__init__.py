from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager


UPLOAD_FOLDER = "flask_blog\static\profile_pics"
ALLOWED_EXTENSIONS = {'png','jpg'}

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "5b4089adff7f5a5c305cda090f6d05f5"
app.config["UPLOAD_FOLDER"]= UPLOAD_FOLDER
db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category="info"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True,
app.config['MAIL_USERNAME'] = "hnyanzi320@gmail.com"
app.config['MAIL_PASSWORD'] = "humphrey320@hum"
mail=Mail(app)



from flask_blog import routes
