from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return "admin"

@admin.route('/<name>/')
def adminName(name):
    return name;

@admin.route('/goldberg/asdf')
def goldbergASDF():
    return "goldberg asdf";
