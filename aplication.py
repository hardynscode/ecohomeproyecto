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

@app.route('/admin/users')
def listadoUsuarios():
    return render_template('./admin/users.html')

@app.route('/admin/houses')
def listadoCasas():
    return render_template('./admin/houses.html')

@app.route('/admin/settings')
def listadoSettings():
    return render_template('./admin/settings/home.html')

@app.route('/admin/settings/tiposTomacorriente')
def listadoSettingsTiposTomacorriente():
    return render_template('./admin/settings/tiposTomacorriente.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)