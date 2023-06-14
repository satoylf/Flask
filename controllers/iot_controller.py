from flask import Blueprint, render_template,redirect,url_for, request, flash
from flask_login import login_required
from models import Sensor, Device, db, Microcontroller 
iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

status = {
        "t": 20.0,
        "h": 30.0,
        "p": 1024.0
        }
# Mensagem de aviso
warn = ""

@iot.route("/")
@login_required
def iot_index():
    return render_template("/admin/iot/iot_index.html")

@iot.route("/status")
@login_required
def iot_status():
    return render_template("/iot/iot_status.html", status = status)

@iot.route("/register_sensor")
@login_required
def register_sensor():
    return render_template("/admin/iot/register_sensor.html")

@iot.route("/view_sensors")
@login_required
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/admin/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
@login_required
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)
    return redirect(url_for("admin.iot.view_sensors"))

@iot.route("/update_sensor/<id>")
@login_required
def update_sensor(id):
    sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(id)).first()

    return render_template("/admin/iot/update_sensor.html", sensor = sensor)

@iot.route("/save_sensor_changes", methods = ["POST"])
@login_required
def save_sensor_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Sensor.update_sensor(data)
    return redirect(url_for("admin.iot.view_sensors"))

@iot.route("/delete_sensor/<id>")
@login_required
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_sensors"))


@iot.route("/register_microcontroller")
def register_microcontroller():
    return render_template("/admin/iot/register_microcontroller.html")

@iot.route("/view_microcontroller")
def view_microcontroller():
    microcontrollers = Microcontroller.get_microcontroller()
    return render_template("/admin/iot/view_microcontroller.html", microcontrollers = microcontrollers)

@iot.route("/save_microcontroller", methods = ["POST"])
def save_microcontroller():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    ports = request.form.get("ports")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Microcontroller.save_microcontroller(name, brand, model, description ,voltage, is_active, ports)
    return redirect(url_for("admin.iot.view_microcontroller"))

@iot.route("/update_microcontroller/<id>")
def update_microcontroller(id):
    microcontroller = db.session.query(Device, Microcontroller)\
                        .join(Microcontroller, Microcontroller.id == Device.id)\
                        .filter(Microcontroller.id == int(id)).first()

    return render_template("/admin/iot/update_microcontroller.html", microcontroller = microcontroller)

@iot.route("/save_microcontroller_changes", methods = ["POST"])
def save_microcontroller_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Microcontroller.update_microcontroller(data)
    return redirect(url_for("admin.iot.view_microcontroller"))

@iot.route("/delete_microcontroller/<id>")
def delete_microcontroller(id):
    if Microcontroller.delete_microcontroller(id):
        flash("Dispositivo Microcontrolador Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Microcontrolador não pode ser excluído!!", "danger")
    return redirect(url_for("admin.iot.view_microcontroller"))
