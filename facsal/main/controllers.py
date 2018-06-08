from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Main Goldberg"

@main.route('/TuFacultad')
def TuFacultad():
    return "Tu Facultad"

@main.route('/TuFacultad/Historia')
def Historia():
    return "/Tu Facultad -> Historia"

@main.route('/TuFacultad/Decanatura')
def Decanatura():
    return "Tu Facultad -> Decanatura"
