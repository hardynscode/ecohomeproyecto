from flask import Flask,render_template, request

app = Flask(__name__)

# Rutas publicas (sin login)
@app.route('/')
def login():
    return render_template('./public/login.html')

@app.route('/forgetpassword')
def forget():
    return render_template('./public/forgetpassword.html')

@app.route('/adduser')
def addser():
    return render_template('./public/adduser.html')

# Rutas para usuarios tipo cliente
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addhome')
def addhome():
    return render_template('addhome.html')

@app.route('/detailshome')
def detailshome():
    idCasa = request.args.get('idCasa')
    return render_template('detailshome.html', idCasa=idCasa)

@app.route('/dcontacto')
def dcontacto():
    return render_template('dcontacto.html')

#Rutas para usuarios tipo admin
@app.route('/admin/home')
def administrativo():
    return render_template('./admin/homeadmin.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)