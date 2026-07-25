from flask import Flask, render_template, Response, request
from ultralytics import YOLO
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)
print("Loading YOLO model...")
model = YOLO("../model/yolov10x.pt")
print("YOLO model loaded!")


def generate_frames():
    while True:
        success, frame = camera.read()
        results = model(frame)
        annotated_frame = results[0].plot()
        if not success:
            break
        ret, buffer = cv2.imencode(".jpg", annotated_frame)
        frame = buffer.tobytes()
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(debug=True)
