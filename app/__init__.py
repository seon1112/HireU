from flask import Flask
# from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy 관련 코드 주석 처리
from config import Config
from datetime import timedelta

# db = SQLAlchemy()  # SQLAlchemy 초기화 주석 처리

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # db.init_app(app)  # SQLAlchemy 초기화 주석 처리


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

    return app
