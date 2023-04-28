from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def  home():
    return render_template('home.html')

@app.route('/periodo')
def periodo():
    return render_template('periodo.html')

@app.route('/facturaepm')
def factura():
    return render_template('factura.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/paginaderegistro')
def paginaderegistro():
    return render_template('paginaderegistro.html')
    
@app.route('/cerrarseion')
def cerrarsesion():
    return render_template('cerrarsesion.html')

@app.route('/administrativo')
def administrativo():
    return render_template('administrativo.html')

if __name__ == '__main__':
    app.run(debug=True)