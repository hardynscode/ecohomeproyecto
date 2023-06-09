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

@app.route('/addfactura')
def addfactura():
    return render_template('addfactura.html')


@app.route('/detailshome')
def detailshome():
    idCasa = request.args.get('idCasa')
    return render_template('detailshome.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/tomacorrientes')
def tomacorrientesHome(idCasa):
    return render_template('listTomacorrientes.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/tomacorrientes/new')
def addTomacorrientesHome(idCasa):
    return render_template('addTomacorriente.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/electrodomesticos')
def electrodomesticosHome(idCasa):
    return render_template('listElectrodomesticos.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/electrodomesticos/new')
def addElectrodomesticoHome(idCasa):
    return render_template('addElectrodomestico.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/electrodomesticos/<idElectrodomestico>/edit')
def updateElectrodomesticoHome(idCasa, idElectrodomestico):
    return render_template('updateElectrodomestico.html', idCasa=idCasa, idElectrodomestico=idElectrodomestico)

@app.route('/detailshome/<idCasa>/electrodomesticos/<idElectrodomestico>/consumo')
def consumoElectrodomesticoHome(idCasa, idElectrodomestico):
    return render_template('consumoElectrodomestico.html', idCasa=idCasa, idElectrodomestico=idElectrodomestico)

@app.route('/detailshome/<idCasa>/addFactura/new')
def addFactura(idCasa):
    return render_template('addFactura.html', idCasa=idCasa)

@app.route('/detailshome/<idCasa>/facturas')
def facturaHome(idCasa):
    return render_template('listFacturas.html', idCasa=idCasa)

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

@app.route('/admin/newUser')
def myNewUser():
    return render_template('./admin/newUser.html')

@app.route('/admin/editUser/<identificacion>')
def myEditUser(identificacion):
    return render_template('./admin/editUser.html', identificacion=identificacion)

@app.route('/admin/settings/tiposRol')
def listadoSettingsTipoRol():
    return render_template('./admin/settings/tipoRol.html')

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

@app.route('/admin/settings/tiposElectrodimesticos')
def listadoSettingsTiposElectrodimesticos():
    return render_template('./admin/settings/tiposElectrodomesticos.html')

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