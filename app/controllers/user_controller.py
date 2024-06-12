from flask import Blueprint,request,jsonify
from app.models.user_model import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

user_bp=Blueprint("user",__name__)

@user_bp.route("/register",methods=["POST"])
def register():
    data=request.json
    name=data.get("name")
    email=data.get("email")
    password=data.get("password")
    phone=data.get("phone")
    role=data.get("role")

    email_ixisting=User.find_by_email(email)
    if email_ixisting:
        return jsonify({"error":"El correo electrónico ya está en uso"}),400
    user=User(name,email,password,phone,role)

    user.save()

    return jsonify({"message":"Usuario creado exitosamente"}),201

@user_bp.route("/login",methods=["POST"])
def login():
    data=request.json
    email=data.get("email")
    password=data.get("password")

    user=User.find_by_email(email)

    if user and check_password_hash(user.password, password):
        access_token=create_access_token(
            identity={"email":email,"role":user.role}
        )
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error":"Credenciales inválidas"}),401
    

    
