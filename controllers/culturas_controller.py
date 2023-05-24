from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Culturas, db
culturas = Blueprint("culturas", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@culturas.route("/")
def culturas_index():
    return render_template("/culturas/culturas_index.html")

@culturas.route("/cadastro_culturas")
def cadastro_culturas():
    return render_template("/culturas/cadastrar_culturas.html")

@culturas.route("/view_culturas")
def view_culturas():
    culturas = Culturas.get_culturas()
    return render_template("/culturas/view_culturas.html", culturas = culturas)

@culturas.route("/save_culturas", methods = ["POST"])
def save_culturas():
    name = request.form.get("name")
    estacao_ideal = request.form.get("estacao_ideal")
    umidade_ideal = request.form.get("umidade_ideal")
    pressao_ideal = request.form.get("pressao_ideal")
    Culturas.save_cultura(name, estacao_ideal, umidade_ideal, pressao_ideal)
    return redirect(url_for('culturas.view_culturas'))

@culturas.route("/delete_cultura/<id>")
def delete_cultura(id):
    if Culturas.delete_cultura(id):
        flash("Cultura Excluído com sucesso!!", "success")
    else:
        flash("Cultura não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("culturas.view_culturas"))

@culturas.route("/update_cultura/<id>")
def update_cultura(id):
    cultura = db.session.query(Culturas).filter(Culturas.id==int(id)).first()
    return render_template("/culturas/update_culturas.html", cultura = cultura)

@culturas.route("/save_cultura_changes", methods = ["POST"])
def save_cultura_changes():
    data = request.form.copy()
    Culturas.update_cultura(data)
    return redirect(url_for("culturas.view_culturas"))
