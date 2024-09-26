# interviewSetting을 따로 뺄까하다가 여기다가 같이 추가하는걸로
from flask import Blueprint, render_template, request, jsonify
#from app.models import db, Interview, Question, Response, Report

interview_bp = Blueprint('interview', __name__)

@interview_bp.route('/interview')
def start_interview():
    return render_template('view_interview.html')

@interview_bp.route('/load_interview_preparation', methods=['GET'])
def load_interview_preparation():
    return render_template('interview_preparation.html')

@interview_bp.route('/load_user_settings', methods=['GET'])
def load_user_settings():
    return render_template('user_settings.html')

@interview_bp.route('/load_interview_process', methods=['GET'])
def load_interview_process():
    return render_template('interview_process.html')

@interview_bp.route('/load_report_generation', methods=['GET'])
def load_report_generation():
    return render_template('report_generation.html')

@interview_bp.route('/load_interview_completion', methods=['GET'])
def load_interview_completion():
    return render_template('interview_completion.html')




##############################################################
@interview_bp.route('/get-question', methods=['GET'])
def get_question():
    question = "여러분이 이 회사에서 꼭 이루고 싶은 목표는 무엇인가요?"
    return jsonify({"question": question})

@interview_bp.route('/submit-answer', methods=['POST'])
def submit_answer():
    user_answer = request.form['answer']
    result = {"status": "success", "message": "Answer submitted successfully"}
    return jsonify(result)
