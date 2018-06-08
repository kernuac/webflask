from flask import Blueprint

admin = Blueprint('admin', __name__)

#/admin/
@admin.route('/')
def index():
    return "admin"
#/admin/name
@admin.route('/<name>/')
def adminName(name):
    return name;
#/admin/goldberg/asdf
@admin.route('/goldberg/asdf')
def goldbergASDF():
    return "goldberg asdf";
