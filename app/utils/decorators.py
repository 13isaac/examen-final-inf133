from functools import wraps
from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request
from flask import jsonify
import json

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args,**kwargs)
        except Exception as e:
            return jsonify({"error":str(e)}),403
    return wrapper

def role_required(role=[]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            try:
                verify_jwt_in_request()
                current_user=get_jwt_identity()
                user_role=json.loads(current_user.get("role"),[])
                if not set(role).intersection(user_role):
                    return jsonify({"error":"Credenciales inválidas"}),401
                return fn(*args,**kwargs)
            except Exception as e:
                return jsonify({"error":str(e)}),403
        return wrapper
    return decorator
