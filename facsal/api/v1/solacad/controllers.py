from flask import Blueprint, jsonify, request
from ..models import SolicitudesAcademicas
import pyodbc

solacad = Blueprint('solacad', __name__)

@solacad.route('/', methods=['GET'])
def index():
    if not request.method == 'GET':
        return jsonify({"status": False});
    return jsonify("solacad");

@solacad.route('/solicitudes/<cod_solicitud>', methods=['GET'])
def get_solicitud(cod_solicitud):
    sol = SolicitudesAcademicas.SolicitudesAcademicas()
    sol.buscarPorId(cod_solicitud)
    return jsonify("ok");
