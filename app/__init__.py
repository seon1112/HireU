from flask import Flask
# from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy 관련 코드 주석 처리
from config import Config
from flask_jwt_extended import JWTManager
from datetime import timedelta

# db = SQLAlchemy()  # SQLAlchemy 초기화 주석 처리

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # db.init_app(app)  # SQLAlchemy 초기화 주석 처리

    # App configurations
    # 토큰 서명에 사용되는 비밀 키
    app.config['JWT_SECRET_KEY'] = "HireU"
    # JWT가 쿠키에 저장됨
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    # 쿠키가 HTTPS에서만 전송되지 않도록 허용 (이거는 개발서버니까)
    app.config['JWT_COOKIE_SECURE'] = False
    # 쿠키 기반 JWT 인증에 CSRF 보호 적용.
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    # Initialize JWT
    jwt = JWTManager(app)

    # 블루프린트 등록
    from .routes.face_recognition_routes import face_recognition_bp
    app.register_blueprint(face_recognition_bp)

    from .routes.make_question_routes import make_question_bp
    app.register_blueprint(make_question_bp)

    from .routes.basic_information_routes import basic_information_bp
    app.register_blueprint(basic_information_bp)
    
    from .routes.history_routes import history_bp
    app.register_blueprint(history_bp)

    from .routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    from .routes.oauth_routes import oauth_bp
    app.register_blueprint(oauth_bp)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    # SQLAlchemy 초기화 코드 주석 처리
    # with app.app_context():
    #     from .models import User, AcssLog, ErrorLog, Interview, Question, Response, Report, ImageFile, VideoFile
    #     db.create_all()

    return app
