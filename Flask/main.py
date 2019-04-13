import cv2
import time
from video import Camera

from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
#Template in the 'templates' folder
	return render_template('index.html')

def gen_frame():
	while True:
		frame = Camera()
		yield (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		time.sleep(0.05)

@app.route('/video_feed')
def video_feed():
	return Response(gen_frame(),
	mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
		app.run(host='0.0.0.0', debug=False)
