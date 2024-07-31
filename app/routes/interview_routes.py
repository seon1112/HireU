# interviewSetting을 따로 뺄까하다가 여기다가 같이 추가하는걸로
from flask import Blueprint, render_template, request, jsonify
from app.models import db, Interview, Question, Response, Report

interview_bp = Blueprint('interview', __name__)

@interview_bp.route('/start-interview', methods=['GET'])
def start_interview():
    return render_template('interview.html')

@interview_bp.route('/get-question', methods=['GET'])
def get_question():
    question = "여러분이 이 회사에서 꼭 이루고 싶은 목표는 무엇인가요?"
    return jsonify({"question": question})

@interview_bp.route('/submit-answer', methods=['POST'])
def submit_answer():
    user_answer = request.form['answer']
    result = {"status": "success", "message": "Answer submitted successfully"}
    return jsonify(result)
