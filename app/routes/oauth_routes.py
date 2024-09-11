from flask import Blueprint, request, render_template, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from config import Config
from app.controller.oauth import Oauth
from app.model.user_model import UserModel, UserData

oauth_bp = Blueprint('oauth', __name__)

@oauth_bp.route("/oauth")
def oauth_api():
    code = str(request.args.get('code'))
    
    oauth = Oauth()
    auth_info = oauth.auth(code)
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    user = UserData(user)
    UserModel().upsert_user(user)

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    # 팝업 창에서 부모 창으로 토큰을 전달하는 자바스크립트
    return f"""
        <script>
            window.opener.postMessage({{
                access_token: '{access_token}', 
                refresh_token: '{refresh_token}'
            }}, window.location.origin);
            window.close();
        </script>
    """


@oauth_bp.route('/oauth/url')
def oauth_url_api():
    return jsonify(
        kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
        % (Config.CLIENT_ID, Config.REDIRECT_URI)
    )


@oauth_bp.route("/oauth/refresh", methods=['POST'])
def oauth_refresh_api():
    refresh_token = request.get_json()['refresh_token']
    result = Oauth().refresh(refresh_token)
    return jsonify(result)


@oauth_bp.route("/oauth/userinfo", methods=['POST'])
def oauth_userinfo_api():
    access_token = request.get_json()['access_token']
    result = Oauth().userinfo("Bearer " + access_token)
    return jsonify(result)
