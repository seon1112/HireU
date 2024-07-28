from flask import Blueprint, render_template

face_recognition_bp = Blueprint('face_recognition', __name__)

@face_recognition_bp.route('/face-recognition')
def face_recognition():
    return render_template('face_recognition.html')