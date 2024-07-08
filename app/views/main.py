from flask import Blueprint, render_template, url_for, redirect
from app.forms.tasa import TasaForm
from app.models.tasa import Tasa
from app.extensions import db

main = Blueprint('main', __name__)

# Index Page
@main.route('/')
def index():
    return render_template('main/index.html')

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
        return redirect(url_for('main.get_tasa'))
    return render_template('main/set_tasa.html', form=form)

# Ver Tasa
@main.route('/tasa/get')
def get_tasa():
    tasa = Tasa.query.order_by(Tasa.id.desc()).first()
    return render_template('main/get_tasa.html', tasa=tasa)