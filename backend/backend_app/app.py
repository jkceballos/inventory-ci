from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_items():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity FROM inventory;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "quantity": r[2]} for r in rows]

@app.route("/items")
def items():
    return jsonify(get_items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
