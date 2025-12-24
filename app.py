import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------------
# CONEXIÓN A POSTGRESQL (RENDER)
# -------------------------
def get_db_connection():
    return psycopg2.connect(
        os.environ.get("DATABASE_URL"),
        sslmode="require"
    )

# -------------------------
# PÁGINA PRINCIPAL
# -------------------------
@app.route("/")
def nuevoindex():
    return render_template("nuevoindex.html")

# -------------------------
# PÁGINAS GENERALES
# -------------------------
@app.route("/trajes")
def trajes():
    return render_template("trajes.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/confirmacion")
def confirmacion():
    return render_template("confirmacion.html")

# -------------------------
# PÁGINAS DE TRAJES
# -------------------------
@app.route("/caporales")
def caporales():
    return render_template("caporales.html")

@app.route("/carnaval")
def carnaval():
    return render_template("carnaval.html")

@app.route("/montonero")
def montonero():
    return render_template("montonero.html")

@app.route("/negrillos")
def negrillos():
    return render_template("negrillos.html")

@app.route("/pampenia")
def pampenia():
    return render_template("pampenia.html")

@app.route("/tinkus")
def tinkus():
    return render_template("tinkus.html")

@app.route("/wakawaka")
def wakawaka():
    return render_template("wakawaka.html")

@app.route("/wititi")
def wititi():
    return render_template("wititi.html")

# -------------------------
# GUARDAR RESERVA (BD ACTIVA)
# -------------------------
@app.route("/guardar_reserva", methods=["POST"])
def guardar_reserva():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reservas (nombre, correo, telefono, traje, parejas, fecha)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            request.form["nombre"],
            request.form["correo"],
            request.form["celular"],
            request.form["danza"],
            int(request.form["parejas"]),
            request.form["fecha"] or None
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("confirmacion"))

    except Exception as e:
        return f"ERROR AL GUARDAR: {e}"

# -------------------------
# EJECUCIÓN
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
