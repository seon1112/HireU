# interviewSetting을 따로 뺄까하다가 여기다가 같이 추가하는걸로
from flask import Blueprint, render_template

interview_bp = Blueprint('interview', __name__)

@interview_bp.route('/interview')
def interview():
    return render_template('interview.html')
