from flask import Blueprint, jsonify
from flask_jwt_extended import (
    get_jwt_identity, jwt_refresh_token_required, 
    create_access_token, set_access_cookies, unset_jwt_cookies, jwt_required
)
from app.model.user_model import UserModel

user_bp = Blueprint('user', __name__)

@user_bp.route('/token/refresh')
@jwt_refresh_token_required
def token_refresh_api():
    user_id = get_jwt_identity()
    resp = jsonify({'result': True})
    access_token = create_access_token(identity=user_id)
    set_access_cookies(resp, access_token)
    return resp


@user_bp.route('/token/remove')
def token_remove_api():
    resp = jsonify({'result': True})
    unset_jwt_cookies(resp)
    resp.delete_cookie('logined')
    return resp


@user_bp.route("/userinfo")
@jwt_required
def userinfo():
    user_id = get_jwt_identity()
    userinfo = UserModel().get_user(user_id).serialize()
    return jsonify(userinfo)
