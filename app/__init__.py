from flask import Flask;
from app.controllers.home import home;

app = Flask(__name__);

app.register_blueprint(home);
