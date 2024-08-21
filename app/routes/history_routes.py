from flask import Blueprint, render_template

history_bp = Blueprint('history', __name__)

@history_bp.route('/history')
def main():
    return render_template('view_history.html')