from flask import Flask, render_template, Response, request
# from motor_control import MotorControl as MC
import cv2
# Initialize the Flask app
app = Flask(__name__)
camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/motor-control', methods=['POST'])
def sendMotorSpeeds():
    if request.method == 'POST':
        vs = request.json["vs"]
        # MC.setSpeed(*vs)
        return 'Sucesss', 200


app.run(debug=True, host="0.0.0.0")
