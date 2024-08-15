from flask import Blueprint, render_template

make_question_bp = Blueprint('make_question', __name__)

@make_question_bp.route('/make_question')
def main():
    return render_template('view_make_question.html')