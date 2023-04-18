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

if __name__ == '__main__':
    app.run(debug=True)