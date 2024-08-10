from flask import Blueprint, render_template, request, Response
import cv2
import pyaudio
import wave
import threading

face_recognition_bp = Blueprint('face_recognition', __name__)

# 카메라 프레임 생성기
def gen_frames(): 
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

def record_audio(output_filename="output.wav", record_seconds=5):
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

    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

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
    t = threading.Thread(target=record_audio)
    t.start()
    return "Recording started"

@face_recognition_bp.route('/')
def index():
    return render_template('face_recognition.html')
