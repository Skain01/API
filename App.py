import uuid
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('personas.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
conn.execute('CREATE TABLE IF NOT EXISTS personas (id TEXT PRIMARY KEY, cedula TEXT NOT NULL UNIQUE, nombre TEXT NOT NULL, edad INTEGER NOT NULL, direccion TEXT)')
conn.close()

@app.route('/', methods=['GET'])
def index():
    return "Home", 200

@app.route('/personas', methods=['POST'])
def crear_persona():
    try:
        data = request.get_json()
        if not data or not all(k in data for k in ("cedula", "nombre", "edad", "direccion")):
            return jsonify({"error": "Faltan datos en la solicitud"}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        nuevo_id = str(uuid.uuid4())

        cur.execute("INSERT INTO personas (id, cedula, nombre, edad, direccion) VALUES (?, ?, ?, ?, ?)", (nuevo_id, data['cedula'], data['nombre'], data['edad'], data['direccion']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Persona creada exitosamente", "id": nuevo_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "La cédula ya existe"}), 400
    except Exception as e:
        return jsonify({"error": f"Error al crear la persona: {str(e)}"}), 500

@app.route('/personas', methods=['GET'])
def obtener_personas():
    conn = get_db_connection()
    personas = conn.execute('SELECT * FROM personas').fetchall()
    conn.close()
    return jsonify([dict(persona) for persona in personas]), 200

@app.route('/personas/<id>', methods=['GET']) #<int:id> se cambia a <id>
def obtener_persona(id):
    conn = get_db_connection()
    persona = conn.execute('SELECT * FROM personas WHERE id = ?', (id,)).fetchone()
    conn.close()
    if persona is None:
        return jsonify({'error': 'Persona no encontrada'}), 404
    return jsonify(dict(persona)), 200

#Modificar info de users
@app.route('/personas/<id>', methods=['PUT']) 
def actualizar_persona(id):
    try:
        data = request.get_json()
        if not data or not all(k in data for k in ("cedula", "nombre", "edad", "direccion")):
            return jsonify({"error": "Faltan datos en la solicitud"}), 400
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE personas SET cedula=?, nombre=?, edad=?, direccion=? WHERE id=?", (data['cedula'], data['nombre'], data['edad'], data['direccion'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Persona actualizada'}), 200
    except Exception as e:
        return jsonify({"error": f"Error al actualizar la persona: {str(e)}"}), 500

# Borrar personas
@app.route('/personas/<id>', methods=['DELETE']) 
def borrar_persona(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM personas WHERE id = ?', (id,))
    conn.commit()
    rows_deleted = cur.rowcount
    conn.close()
    if rows_deleted > 0:
        return jsonify({"message": "Usuario borrado correctamente"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)