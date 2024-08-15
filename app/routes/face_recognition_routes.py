import os
from flask import Blueprint, render_template, request, Response, send_file, abort
import cv2
import pyaudio
import wave
import threading

face_recognition_bp = Blueprint('face_recognition', __name__)

is_recording = False
output_filename = os.path.join(os.path.dirname(__file__), 'output.wav')  # 절대 경로로 설정

def gen_frames():  # 카메라 프레임 생성기
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@face_recognition_bp.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def record_audio(output_filename="output.wav"):
    global is_recording

    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []

    print("Recording started...")
    while is_recording:
        data = stream.read(chunk)
        frames.append(data)
    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

@face_recognition_bp.route('/start_audio_recording', methods=['POST'])
def start_audio_recording():
    global is_recording
    is_recording = True
    t = threading.Thread(target=record_audio, args=(output_filename,))
    t.start()
    return "Recording started"

@face_recognition_bp.route('/stop_audio_recording', methods=['POST'])
def stop_audio_recording():
    global is_recording
    is_recording = False
    return "Recording stopped"

@face_recognition_bp.route('/play_audio')
def play_audio():
    if os.path.exists(output_filename):
        return send_file(output_filename, as_attachment=False)
    else:
        return abort(404, description="File not found")
    
@face_recognition_bp.route('/face_recognition')
def index():
    return render_template('face_recognition.html')
