from flask import Flask, jsonify, request

from repositories.persona_repository import PersonaRepository
from services.persona_service import PersonaService


app = Flask(__name__)


# ==========================================
# Dependencias
# ==========================================

persona_repository = PersonaRepository()

persona_service = PersonaService(
    persona_repository
)


# ==========================================
# GET - obtener todas las personas
# ==========================================

@app.route("/personas", methods=["GET"])
def obtener_personas():

    personas = persona_service.obtener_todos()

    return jsonify(personas), 200


# ==========================================
# GET - obtener una persona
# ==========================================

@app.route("/personas/<dni>", methods=["GET"])
def obtener_persona(dni):

    resultado = persona_service.obtener_por_dni(dni)

    if not resultado["ok"]:
        return jsonify(resultado), 404

    return jsonify(resultado), 200


# ==========================================
# POST - crear persona
# ==========================================

@app.route("/personas", methods=["POST"])
def crear_persona():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "ok": False,
            "mensaje": "No se enviaron datos"
        }), 400

    dni = datos.get("dni")
    nombre = datos.get("nombre")

    resultado = persona_service.crear(
        dni,
        nombre
    )

    if not resultado["ok"]:
        return jsonify(resultado), 400

    return jsonify(resultado), 201


# ==========================================
# PUT - modificar persona
# ==========================================

@app.route("/personas/<dni>", methods=["PUT"])
def actualizar_persona(dni):

    datos = request.get_json()

    if not datos:
        return jsonify({
            "ok": False,
            "mensaje": "No se enviaron datos"
        }), 400

    nombre = datos.get("nombre")

    resultado = persona_service.actualizar(
        dni,
        nombre
    )

    if not resultado["ok"]:
        return jsonify(resultado), 400

    return jsonify(resultado), 200


# ==========================================
# DELETE - eliminar persona
# ==========================================

@app.route("/personas/<dni>", methods=["DELETE"])
def eliminar_persona(dni):

    resultado = persona_service.eliminar(dni)

    if not resultado["ok"]:
        return jsonify(resultado), 404

    return jsonify(resultado), 200


# ==========================================
# Ejecutar Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)