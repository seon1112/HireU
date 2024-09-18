# 여기에다가 gpt API도 같이
from flask import Blueprint, render_template

report_bp = Blueprint('report', __name__)

@report_bp.route('/report')
def interview():
    return render_template('view_report.html')