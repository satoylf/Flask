from flask import Blueprint, render_template,redirect,url_for

culturas = Blueprint("culturas", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@culturas.route("/")
def culturas_index():
    return render_template("/culturas/culturas_index.html")