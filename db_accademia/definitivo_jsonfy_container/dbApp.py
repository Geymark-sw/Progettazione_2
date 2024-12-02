from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Dettagli di connessione al database
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'Accademia',
    'user': 'postgres',
    'password': 'postgres'
}

def get_db_connection():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        return str(e)


def execute(query: str):
    connection = get_db_connection()
    if isinstance(connection, str):  # errore durante la connessione
        return jsonify({"error": connection}), 500

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()



query = ""
@app.route("/1")
def query1():
#if scelta == "1":
    query = "SELECT DISTINCT ass.tipo FROM Assenza ass"
    connection = get_db_connection()
    if isinstance(connection, str):  # errore durante la connessione
        return jsonify({"error": connection}), 500

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route("/2")
def query2():
    #elif scelta == "2":
    query = "SELECT DISTINCT annop.giorno FROM AttivitaNonProgettuale annop WHERE annop.tipo = 'Didattica' ORDER BY annop.giorno ASC"
    execute(query)

@app.route("/3")
def query3():    
    #elif scelta == "3":
    query = "SELECT wp.nome, wp.inizio, wp.fine FROM Wp wp JOIN Progetto pr ON pr.id = wp.progetto WHERE pr.nome = 'Pegasus'"
    execute(query)
    #else:
        #return jsonify({"error": "Scelta non valida"}), 400


@app.route('/')
def home():
    return "Benvenuto! Vai su /query?scelta=1 per eseguire una query."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
