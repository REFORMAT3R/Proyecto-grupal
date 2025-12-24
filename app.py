from flask import Flask, render_template,request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# Página principal
@app.route('/')
def nuevoindex():
    return render_template('nuevoindex.html')

#Página de trajes folklóricos
@app.route('/trajes')
def trajes():
    return render_template('trajes.html')

# Página de contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Páginas de trajes específicos
@app.route('/wititi')
def wititi():
    return render_template('wititi.html')

@app.route('/tinkus')
def tinkus():
    return render_template('tinkus.html')

@app.route('/pampenia')
def pampenia():
    return render_template('pampenia.html')

@app.route('/negrillos')
def negrillos():
    return render_template('negrillos.html')

@app.route('/wakawaka')
def wakawaka():
    return render_template('wakawaka.html')
@app.route('/carnaval')
def carnaval():
    return render_template('carnaval.html')
@app.route('/montonero')
def montonero():
    return render_template('montonero.html')
@app.route('/caporales')
def caporales():
    return render_template('caporales.html')

#Formulario de reserva de trajes
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        traje = request.form['traje']
        mensaje = request.form['mensaje']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO reservas (nombre, correo, telefono, traje, mensaje)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, correo, telefono, traje, mensaje))

        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('nuevoindex'))

    return render_template('formulario.html')


if __name__ == "__main__":
    app.run()
