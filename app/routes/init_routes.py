from .main_routes import main_bp
from .login_routes import login_bp
from .extract_audio_routes import question_bp
from .face_recognition_routes import face_recognition_bp
from .interview_routes import interview_bp
from .main_routes import result_bp
from .report_routes import mypage_bp

def init_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(face_recognition_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(result_bp)
    app.register_blueprint(mypage_bp)
