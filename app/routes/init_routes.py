from .main_routes import main_bp
from .extract_audio_routes import extract_audio_bp
from .face_recognition_routes import face_recognition_bp
from .interview_routes import interview_bp
from .report_routes import report_bp
from .basic_information_routes import basic_information_bp
from .history_routes import history_bp

def init_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(extract_audio_bp)
    app.register_blueprint(face_recognition_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(basic_information_bp)
    app.register_blueprint(history_bp)