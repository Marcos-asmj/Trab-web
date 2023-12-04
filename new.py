import MySQLdb
from flask import Flask, jsonify, request, g, current_app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = MySQLdb.connect(host="localhost", user="root", passwd="j7561opp", db="football_db")

@app.route('/players', methods=['GET'])
def get_players():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM players")
        players_data = cursor.fetchall()
        return jsonify({"players_data": players_data})
    except Exception as e:
        return jsonify({"error": f"Erro ao executar SELECT: {e}"})
    finally:
        cursor.close()

@app.route('/players', methods=['POST'])
def add_player():
    try:
        cursor = db.cursor()
        data = request.json 
        cursor.execute("INSERT INTO players (name, team, games_played, yellow_cards, red_cards) VALUES (%s, %s, %s, %s, %s)",
                       (data['name'], data['team'], data['games_played'], data['yellow_cards'], data['red_cards']))
        db.commit()
        return jsonify({"message": "Inserção bem-sucedida."})
    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Erro ao executar INSERT: {e}"})
    finally:
        cursor.close()

@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    try:
        cursor = db.cursor()
        data = request.json
        cursor.execute("UPDATE players SET name=%s, team=%s, games_played=%s, yellow_cards=%s, red_cards=%s WHERE id=%s",
                       (data['name'], data['team'], data['games_played'], data['yellow_cards'], data['red_cards'], player_id))
        db.commit()
        return jsonify({"message": "Atualização bem-sucedida."})
    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Erro ao executar UPDATE: {e}"})
    finally:
        cursor.close()

@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM players WHERE id=%s", (player_id,))
        db.commit()
        return jsonify({"message": "Exclusão bem-sucedida."})
    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Erro ao executar DELETE: {e}"})
    finally:
        cursor.close()

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)
