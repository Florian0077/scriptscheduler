from flask import Flask, request, jsonify, render_template
from scheduler import Scheduler
from database import db_session
from models import Script, Log

app = Flask(__name__)
scheduler = Scheduler()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_script", methods=["POST"])
def add_script():
    data = request.json
    script = Script(
        name=data["name"],
        path=data["path"],
        schedule=data["schedule"],
        active=data.get("active", True),  # Par défaut, le script est actif
        venv_path=data["venv_path"],
    )
    db_session.add(script)
    db_session.commit()
    if script.active:
        scheduler.add_job(script)
    return jsonify({"message": "Script ajouté avec succès"}), 201


@app.route("/remove_script/<int:script_id>", methods=["DELETE"])
def remove_script(script_id):
    script = Script.query.get(script_id)
    if script:
        scheduler.remove_job(script)
        db_session.delete(script)
        db_session.commit()
        return jsonify({"message": "Script supprimé avec succès"}), 200
    return jsonify({"message": "Script non trouvé"}), 404


@app.route("/toggle_script/<int:script_id>", methods=["POST"])
def toggle_script(script_id):
    script = Script.query.get(script_id)
    if script:
        script.active = not script.active
        db_session.commit()
        if script.active:
            scheduler.add_job(script)
        else:
            scheduler.remove_job(script)
        return (
            jsonify(
                {"message": "Statut du script mis à jour", "active": script.active}
            ),
            200,
        )
    return jsonify({"message": "Script non trouvé"}), 404


@app.route("/list_scripts", methods=["GET"])
def list_scripts():
    scripts = Script.query.all()
    return jsonify([s.to_dict() for s in scripts])


@app.route("/run_script_now/<int:script_id>", methods=["POST"])
def run_script_now(script_id):
    script = Script.query.get(script_id)
    if script:
        try:
            # Utiliser la méthode execute_script du scheduler
            scheduler.execute_script(script)
            return (
                jsonify({"message": f"Script '{script.name}' exécuté avec succès"}),
                200,
            )
        except Exception as e:
            return (
                jsonify({"message": f"Erreur lors de l'exécution du script: {str(e)}"}),
                500,
            )
    return jsonify({"message": "Script non trouvé"}), 404


@app.route("/get_logs", methods=["GET"])
def get_logs():
    # Récupérer les paramètres de pagination
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    # Calculer les logs à récupérer
    query = Log.query.order_by(Log.timestamp.desc())
    total_logs = query.count()
    logs = query.offset((page - 1) * per_page).limit(per_page).all()

    # Calculer le nombre total de pages
    total_pages = (total_logs + per_page - 1) // per_page

    # Retourner les logs avec les informations de pagination
    return jsonify(
        {
            "logs": [log.to_dict() for log in logs],
            "total": total_logs,
            "pages": total_pages,
            "current_page": page,
        }
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
