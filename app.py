from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def nuevoindex():
    return render_template('nuevoindex.html')

@app.route('/trajes')
def trajes():
    return render_template('trajes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

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
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == "__main__":
    app.run()
