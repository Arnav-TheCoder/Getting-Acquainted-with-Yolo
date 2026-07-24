from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import cv2
import os
import uuid

app = Flask(__name__)

# ----------------------------
# Configuration
# ----------------------------
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
MODEL_PATH = "../model/yolov10x.pt"
# MODEL_PATH = "model/yolo11x.pt"
# MODEL_PATH = "model/yolo26x.pt"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# ----------------------------
# Load YOLO Model (Loads Once)
# ----------------------------
print("Loading YOLO Model...")
model = YOLO(MODEL_PATH)
print("YOLO Model Loaded Successfully!")

# ----------------------------
# Helper Functions (utils.py merged here)
# ----------------------------

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "webp"}


def allowed_file(filename):
    """
    Check whether uploaded file has an allowed extension.
    """
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def generate_filename(filename):
    """
    Generate unique filename to avoid duplicates.
    """
    extension = filename.rsplit(".", 1)[1]
    return f"{uuid.uuid4().hex}.{extension}"


def detect_objects(image_path, output_path):
    """
    Runs YOLO inference, draws bounding boxes,
    saves output image and returns detection data.
    """

    results = model(image_path)

    result = results[0]

    annotated = result.plot()

    cv2.imwrite(output_path, annotated)

    detections = []

    for box in result.boxes:

        class_id = int(box.cls[0])

        class_name = model.names[class_id]

        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        detections.append(
            {
                "class": class_name,
                "confidence": round(confidence * 100, 2),
                "box": [x1, y1, x2, y2]
            }
        )

    return detections


# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():

    return render_template(
        "index.html",
        uploaded_image=None,
        result_image=None,
        detections=None
    )


@app.route("/detect", methods=["POST"])
def detect():

    if "image" not in request.files:
        return redirect("/")

    file = request.files["image"]

    if file.filename == "":
        return redirect("/")

    if not allowed_file(file.filename):
        return redirect("/")

    filename = generate_filename(file.filename)

    upload_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    result_path = os.path.join(
        app.config["RESULT_FOLDER"],
        filename
    )

    file.save(upload_path)

    detections = detect_objects(
        upload_path,
        result_path
    )

    return render_template(
        "index.html",
        uploaded_image=filename,
        result_image=filename,
        detections=detections
    )


# ----------------------------
# Serve Uploaded Images
# ----------------------------

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    from flask import send_from_directory

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


@app.route("/results/<filename>")
def result_file(filename):
    from flask import send_from_directory

    return send_from_directory(
        app.config["RESULT_FOLDER"],
        filename
    )


# ----------------------------
# Main
# ----------------------------

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
