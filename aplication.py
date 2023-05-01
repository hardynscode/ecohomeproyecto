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

@app.route('/admin/settings/tiposCasas')
def listadoSettingsTiposCasas():
    return render_template('./admin/settings/tiposCasas.html')

@app.route('/admin/settings/zonasCasas')
def listadoSettingsZonasCasas():
    return render_template('./admin/settings/zonasCasas.html')

@app.route('/admin/settings/tiposEficiencia')
def listadoSettingsTiposEficiencia():
    return render_template('./admin/settings/tiposEficiencia.html')

@app.route('/admin/settings/paises')
def listadoSettingsPaises():
    return render_template('./admin/settings/paises.html')

@app.route('/admin/settings/paises/<pais>/departamentos', methods=['GET'])
def listadoSettingsDepartamentos(pais):
    return render_template('./admin/settings/departamentos.html', pais=pais)

@app.route('/admin/settings/paises/<pais>/departamentos/<departamento>/ciudades', methods=['GET'])
def listadoSettingsCiudades(pais, departamento):
    return render_template('./admin/settings/ciudades.html', pais=pais, departamento=departamento)

if __name__ == '__main__':
    app.run(debug=True, port=5001)