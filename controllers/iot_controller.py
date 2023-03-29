from flask import Blueprint, render_template,redirect,url_for

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/cadastro_cultura")
def iot_cadastro():
    return render_template("/iot/iot_cadastrar_cultura.html")
