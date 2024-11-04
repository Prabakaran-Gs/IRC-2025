from flask import Blueprint, render_template, Response
import random
import cv2

main = Blueprint('main', __name__)

# Initialize the camera
camera = cv2.VideoCapture(0)

# Route to generate frames for video feed
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/')
def index():
    return render_template('dashboard.html')

@main.route('/science-subsystem')
def science_subsystem():
    data = {
        "MQ_8": {"value": 0},
        "MQ_9": {"percentage": 0, "stroke_dasharray": f"{0}, {100}"},
        "MQ_135": {"value": 0},
        "BME680": {"temperature": 0, "humidity": 0, "pressure": 0, "voc": 0},
        "SOIL_MOISTURE": {"value": 0, "stroke_dasharray": f"{0}, {100}"},
        "SOIL_TEMPERATURE": 0,
        "pH_Level": 0,
        "NPK_SENSOR": {"nitrogen": 0, "phosphorus": 0, "potassium": 0}
    }
    return render_template('science.html', data=data)

@main.route('/power-subsystem')
def power_subsystem():
    return render_template('power.html')

@main.route('/control-subsystem')
def control_subsystem():
    return render_template('control.html')

@main.route('/science-subsystem/hydrogen-concentration')
def hydrogen_concentration_data():
    val = random.randint(100, 10000)
    return {"hydrogen_concentration": val}

@main.route('/science-subsystem/combustible-gases')
def combustible_gases_data():
    val = random.randint(0, 100)
    return {"combustible_gases": val}

@main.route('/science-subsystem/pH-Level')
def pH_Level_data():
    val = random.randint(0, 14)
    return {"pH_Level": val}

@main.route('/science-subsystem/air-quality')
def air_quality_data():
    val = random.randint(10, 1000)
    return {"air_quality": val}

@main.route('/science-subsystem/soil-moisture')
def soil_moisture_data():
    val = random.randint(0, 100)
    return {"soil_moisture": val}

@main.route('/science-subsystem/soil-temperature')
def soil_temperature_data():
    val = random.randint(-40, 125)
    return {"soil_temperature": val}

@main.route('/science-subsystem/NPK')
def NPK_data():
    NPK = {"nitrogen": random.randint(0, 1000), "phosphorus": random.randint(0, 100), "potassium": random.randint(0, 1000)}
    return NPK

@main.route('/science-subsystem/BME680')
def BME680_data():
    BME680 = {"temperature": random.randint(-40, 85), "humidity": random.randint(0, 100), "pressure": random.randint(30000, 110000), "voc": random.randint(0,500)}
    return BME680

@main.route('/video_feed')
def video_feed():
    # Route for video feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
