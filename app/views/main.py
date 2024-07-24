from flask import Blueprint, render_template, url_for, redirect, request
from app.forms.tasa import TasaForm
from app.models.tasa import Tasa
from app.forms.caja import CajaForm
from app.models.caja import Caja
from app.forms.opwu import OpWuForm
from app.models.opwu import OpWu
from app.extensions import db

main = Blueprint('main', __name__)

# Index Page
@main.route('/')
def index():
    #valor más actual de la tasa
    tasa = Tasa.query.order_by(Tasa.id.desc()).first()
    return render_template('main/index.html',tasa=tasa)

# Fijar Tasa
@main.route('/tasa/set', methods=['GET', 'POST'])
def set_tasa():
    form = TasaForm()
    if form.validate_on_submit():
        new_tasa = Tasa(
            tasa_oficial=form.tasa_oficial.data,
            tasa_compra=form.tasa_compra.data,
            tasa_venta=form.tasa_venta.data,
            tasa_wu=form.tasa_wu.data
        )
        db.session.add(new_tasa)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('main/set_tasa.html', form=form)

# Ver Tasa
@main.route('/tasa/get')
def get_tasa():
    tasa = Tasa.query.order_by(Tasa.id.desc()).first()
    return render_template('main/get_tasa.html', tasa=tasa)

### CAJA
def get_total():
    caja = Caja.query.order_by(Caja.id.desc()).first()
    total_local = 0
    total_local += caja.moneda_local_1
    total_local += caja.moneda_local_5 * 5
    total_local += caja.moneda_local_10 * 10
    total_local += caja.moneda_local_20 * 20
    total_local += caja.moneda_local_50 * 50
    total_local += caja.moneda_local_100 * 100
    total_local += caja.moneda_local_200 * 200
    total_local += caja.moneda_local_500 * 500
    total_local += caja.moneda_local_1000 * 1000
    total_dolar = 0
    total_dolar += caja.dolar_1
    total_dolar += caja.dolar_5 * 5
    total_dolar += caja.dolar_10 * 10
    total_dolar += caja.dolar_20 * 20
    total_dolar += caja.dolar_50 * 50
    total_dolar += caja.dolar_100 * 100
    return {'total_local': total_local, 'total_dolar': total_dolar}

# Caja SET
@main.route('/caja/get')
def get_caja():
    caja = Caja.query.order_by(Caja.id.desc()).first()
    total = get_total()
    return render_template('main/get_caja.html', caja=caja, total=total)

# Caja GET
@main.route('/caja/set', methods=['GET', 'POST'])
def set_caja():
    form = CajaForm()
    if form.validate_on_submit():
        nueva_caja = Caja(
            moneda_local_1=form.moneda_local_1.data,
            moneda_local_5=form.moneda_local_5.data,
            moneda_local_10=form.moneda_local_10.data,
            moneda_local_20=form.moneda_local_20.data,
            moneda_local_50=form.moneda_local_50.data,
            moneda_local_100=form.moneda_local_100.data,
            moneda_local_200=form.moneda_local_200.data,
            moneda_local_500=form.moneda_local_500.data,
            moneda_local_1000=form.moneda_local_1000.data,
            dolar_1=form.dolar_1.data,
            dolar_5=form.dolar_5.data,
            dolar_10=form.dolar_10.data,
            dolar_20=form.dolar_20.data,
            dolar_50=form.dolar_50.data,
            dolar_100=form.dolar_100.data
        )
        db.session.add(nueva_caja)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('main/set_caja.html', form=form)


# Operaciones Western Union
@main.route('/wu/operaciones_wu',methods=['GET','POST'])
def operaciones_wu():

    form = OpWuForm()

    if request.method == 'POST':
        #get data from form
        tipo_operacion = request.form['tipo_operacion']
        codigo_mtcn = request.form['codigo_mtcn']
        transaccion = request.form['transaccion']
        montotrus = float(request.form['montotrus'])
        montopus = float(request.form['montopus'])
        montotrcs = float(request.form['montotrcs'])
        montopcs = float(request.form['montopcs'])   

        #save data in table 
        nueva_operacion = OpWu(
            transaccion=transaccion,
            codigo_mtcn=codigo_mtcn,
            tipo_operacion=tipo_operacion,
            montotrus=montotrus,
            montopus=montopus,
            montotrcs=montotrcs,
            montopcs=montopcs
        )

        db.session.add(nueva_operacion)
        db.session.commit()

        return redirect(url_for('main.index'))
    else:
        return render_template('main/operaciones_wu.html', form = form, ultima_tasa = Tasa.query.order_by(Tasa.id.desc()).first())

# Historial de Operaciones Western Union
@main.route('/wu/historial')
def historial_wu():
    historial = OpWu.query.all()
    return render_template('main/historial_wu.html', historial=historial)