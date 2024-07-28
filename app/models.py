from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(255), primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    refresh_token = db.Column(db.Text)
    industry = db.Column(db.String(255))
    job_position = db.Column(db.String(255))
    technical_skills = db.Column(db.Text)
    major = db.Column(db.Text)
    certifications = db.Column(db.Text)
    special_experience = db.Column(db.Text)
    cover_letter = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    interviews = db.relationship('Interview', backref='user', lazy=True)
    acss_logs = db.relationship('AcssLog', backref='user', lazy=True)
    error_logs = db.relationship('ErrorLog', backref='user', lazy=True)

class AcssLog(db.Model):
    __tablename__ = 'acss_log'
    acss_log_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('users.user_id'))
    acss_ip = db.Column(db.String(20))
    log_txt = db.Column(db.Text)
    acss_at = db.Column(db.DateTime, default=datetime.utcnow)

class ErrorLog(db.Model):
    __tablename__ = 'error_log'
    error_log_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('users.user_id'))
    error_ip = db.Column(db.String(20))
    error_url = db.Column(db.String(200))
    error_txt = db.Column(db.Text)
    error_at = db.Column(db.DateTime, default=datetime.utcnow)

class Interview(db.Model):
    __tablename__ = 'interviews'
    interview_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interview_nm = db.Column(db.String(256))
    user_id = db.Column(db.String(255), db.ForeignKey('users.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    questions = db.relationship('Question', backref='interview', lazy=True)
    responses = db.relationship('Response', backref='interview', lazy=True)
    reports = db.relationship('Report', backref='interview', lazy=True)

class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.Text, nullable=False)
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.interview_id'))
    responses = db.relationship('Response', backref='question', lazy=True)
    reports = db.relationship('Report', backref='question', lazy=True)

class Response(db.Model):
    __tablename__ = 'responses'
    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.interview_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    response_text = db.Column(db.Text)

class Report(db.Model):
    __tablename__ = 'reports'
    report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.interview_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    morpheme = db.Column(db.Text)
    cloud_grap = db.Column(db.Integer, db.ForeignKey('image_files.file_seq'))
    face_image = db.Column(db.Integer, db.ForeignKey('image_files.file_seq'))
    smile = db.Column(db.String(10))
    angry = db.Column(db.String(10))
    sad = db.Column(db.String(10))
    face_less = db.Column(db.String(10))
    speaking_speed = db.Column(db.String(255))
    video_seq = db.Column(db.Integer, db.ForeignKey('video_files.video_seq'))
    total_comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ImageFile(db.Model):
    __tablename__ = 'image_files'
    file_seq = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_file_nm = db.Column(db.String(200), nullable=False)
    sys_file_nm = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    reg_id = db.Column(db.String(50), nullable=False)
    reg_dt = db.Column(db.DateTime, default=datetime.utcnow)
    down_num = db.Column(db.Integer, default=0)

class VideoFile(db.Model):
    __tablename__ = 'video_files'
    video_seq = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_file_nm = db.Column(db.String(200), nullable=False)
    sys_file_nm = db.Column(db.String(200), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    reg_id = db.Column(db.String(50), nullable=False)
    reg_dt = db.Column(db.DateTime, default=datetime.utcnow)
