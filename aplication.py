from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/addhome')
def addhome():
    return render_template('addhome.html')

@app.route('/periodo')
def periodo():
    return render_template('periodo.html')

@app.route('/facturaepm')
def factura():
    return render_template('factura.html')

@app.route('/dcontacto')
def dcontacto():
    return render_template('dcontacto.html')

@app.route('/paginaderegistro')
def paginaderegistro():
    return render_template('paginaderegistro.html')
    
@app.route('/cerrarseion')
def cerrarsesion():
    return render_template('cerrarsesion.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)