from flask import Flask, jsonify, request
from config import db, app
from models import Pokemon
from get_files import connect_to_server
from handle_query import get_all_answers
from handle_query import run_user_query_on_db

@app.route("/pokemons", methods=["GET"])
def get_contact():
    pokemon = Pokemon.query.all()
    json_pokemons = list(map(lambda x: x.to_json(), pokemon))
    return jsonify({"Pokemons": json_pokemons})

@app.route("/create", methods=["POST"])
def create():
    try:
        data = request.get_json()
        user_url = data.get("query", "")
        return jsonify({"message": "Database is created", "data":f"{connect_to_server(151, user_url)}"})
    except Exception as e:
        return jsonify({"message": "Error", "data": f"{str(e)}"}), 500

@app.route("/generate", methods=["POST"])
def generate():
    try:
        final_answers = get_all_answers()
        return jsonify({
            "message": "Database search done",
            "data": final_answers or " No data generated."
        })
    except Exception as e:
        print("ERROR in /generate:", e)
        return jsonify({"message": "Error", "data": f"{str(e)}"}), 500
    
@app.route("/query", methods=["POST"])
def run_user_query():
    try:
        data = request.get_json()
        user_query = data.get("query", "")
        result = run_user_query_on_db(user_query)
        return jsonify({"message": "Query executed", "data": result})
    except Exception as e:
        print("ERROR in /query:", e)
        return jsonify({"message": "Error", "data": str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
