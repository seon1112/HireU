from flask import Blueprint, render_template

basic_information_bp = Blueprint('basic_information', __name__)

@basic_information_bp.route('/basic_information')
def main():
    return render_template('view_basic_information.html')