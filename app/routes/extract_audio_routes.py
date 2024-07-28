# 오디오 추출해서 텍스트 분석, 말의 속도 분석 여기서
from flask import Blueprint, render_template

face_recognition_bp = Blueprint('extract_audio', __name__)

@face_recognition_bp.route('/extract_audio')
def face_recognition():
    return render_template('extract_audio.html')
