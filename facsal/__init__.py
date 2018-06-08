from flask import Flask;
from facsal.main.controllers import main;
from facsal.admin.controllers import admin;
from facsal.api.v1.solacad.controllers import solacad as cSolacad;

app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin');
app.register_blueprint(cSolacad, url_prefix='/api/v1/solacad');
app.register_blueprint(main);


