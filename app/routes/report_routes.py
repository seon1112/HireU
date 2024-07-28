# 여기에다가 gpt API도 같이
from flask import Blueprint, render_template

interview_bp = Blueprint('report', __name__)

@interview_bp.route('/report')
def interview():
    return render_template('report.html')