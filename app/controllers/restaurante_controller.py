from app.models.restaurante_model import Restaurante
from app.utils.decorators import jwt_required,role_required
from flask import jsonify,Blueprint,request
from app.views.restaurante_view import render_detail_restaurante,render_list_restaurantes

restaurante_bp=Blueprint("restaurante",__name__)

@restaurante_bp.route("/restaurants",methods=["GET"])
@jwt_required
@role_required(role=["customer","admin"])
def get_restaurantes():
    restaurantes=Restaurante.get_all()
    return jsonify(render_list_restaurantes(restaurantes))

@restaurante_bp.route("/restaurants/<int:id>",methods=["GET"])
@jwt_required
@role_required(role=["customer","admin"])
def get_restaurante(id):
    restaurante=Restaurante.get_by_id(id)

    if restaurante:
        return jsonify(render_detail_restaurante(restaurante))
    return jsonify({"error":"Restaurante no encontrado"}),404

@restaurante_bp.route("/restaurants",methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def create_restaurante():
    data=request.json
    name=data.get("name")
    address=data.get("address")
    city=data.get("city")
    phone=data.get("phone")
    description=data.get("description")
    rating=data.get("rating")

    if name is None or address is None or city is None or phone is None or description is None or rating is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    
    restaurante=Restaurante(name,address,city,phone,description,rating)
    restaurante.save()

    return jsonify({"message":"Restaurante creado existosamente"}),201

@restaurante_bp.route("/restaurants/<int:id>",methods=["PUT"])
@jwt_required
@role_required(role=["admin"])
def update_restaurante(id):
    rest=Restaurante.get_by_id(id)

    if not rest:
        return jsonify({"error":"Restaurante no encontrado"}),404
    data=request.json
    name=data.get("name")
    address=data.get("address")
    city=data.get("city")
    phone=data.get("phone")
    description=data.get("description")
    rating=data.get("rating")

    rest.update(name,address,city,phone,description,rating)

    return jsonify(render_detail_restaurante(rest))

@restaurante_bp.route("/restaurants/<int:id>",methods=["DELETE"])
@jwt_required
@role_required(role=["admin"])
def delete_restaurante(id):
    rest=Restaurante.get_by_id(id)

    if not rest:
        return jsonify({"error":"Restaurante no encontrado"}),404
    rest.delete()
    return "",204