from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # 블루프린트 등록
    from .routes.face_recognition_routes import face_recognition_bp
    app.register_blueprint(face_recognition_bp)

    # SQLAlchemy 초기화
    with app.app_context():
        from .models import User, AcssLog, ErrorLog, Interview, Question, Response, Report, ImageFile, VideoFile
        db.create_all()

    return app
