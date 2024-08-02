from flask_sqlalchemy import SQLAlchemy
from flask import request

db = SQLAlchemy()


def alterar_caja(Caja,inputs):
    caja = Caja.query.order_by(Caja.id.desc()).first()
    caja.moneda_local_1 += inputs['moneda_local_1']
    caja.moneda_local_5 += inputs['moneda_local_5']
    caja.moneda_local_10 += inputs['moneda_local_10']
    caja.moneda_local_20 += inputs['moneda_local_20']
    caja.moneda_local_50 += inputs['moneda_local_50']
    caja.moneda_local_100 += inputs['moneda_local_100']
    caja.moneda_local_200 += inputs['moneda_local_200']
    caja.moneda_local_500 += inputs['moneda_local_500']
    caja.moneda_local_1000 += inputs['moneda_local_1000']
    caja.dolar_1 += inputs['dolar_1']
    caja.dolar_5 += inputs['dolar_5']
    caja.dolar_10 += inputs['dolar_10']
    caja.dolar_20 += inputs['dolar_20']
    caja.dolar_50 += inputs['dolar_50']
    caja.dolar_100 += inputs['dolar_100']
    db.session.commit()

def transaction_balance(inputs):
    token = {}
    token['moneda_local_1'] = inputs['montoi_1_CS'] - inputs['montos_1_CS']
    token['moneda_local_5'] = inputs['montoi_5_CS'] - inputs['montos_5_CS']
    token['moneda_local_10'] = inputs['montoi_10_CS'] - inputs['montos_10_CS']
    token['moneda_local_20'] = inputs['montoi_20_CS'] - inputs['montos_20_CS']
    token['moneda_local_50'] = inputs['montoi_50_CS'] - inputs['montos_50_CS']
    token['moneda_local_100'] = inputs['montoi_100_CS'] - inputs['montos_100_CS']
    token['moneda_local_200'] = inputs['montoi_200_CS'] - inputs['montos_200_CS']
    token['moneda_local_500'] = inputs['montoi_500_CS'] - inputs['montos_500_CS']
    token['moneda_local_1000'] = inputs['montoi_1000_CS'] - inputs['montos_1000_CS']
    token['dolar_1'] = inputs['montoi_1_US'] - inputs['montos_1_US']
    token['dolar_5'] = inputs['montoi_5_US'] - inputs['montos_5_US']
    token['dolar_10'] = inputs['montoi_10_US'] - inputs['montos_10_US']
    token['dolar_20'] = inputs['montoi_20_US'] - inputs['montos_20_US']
    token['dolar_50'] = inputs['montoi_50_US'] - inputs['montos_50_US']
    token['dolar_100'] = inputs['montoi_100_US'] - inputs['montos_100_US']
    return token

def get_transaction_values():
    token = {}
    token['montoi_1_CS'] = float(request.form['montoi_1_CS'])
    token['montoi_5_CS'] = float(request.form['montoi_5_CS'])
    token['montoi_10_CS'] = float(request.form['montoi_10_CS'])
    token['montoi_20_CS'] = float(request.form['montoi_20_CS'])
    token['montoi_50_CS'] = float(request.form['montoi_50_CS'])
    token['montoi_100_CS'] = float(request.form['montoi_100_CS'])
    token['montoi_200_CS'] = float(request.form['montoi_200_CS'])
    token['montoi_500_CS'] = float(request.form['montoi_500_CS'])
    token['montoi_1000_CS'] = float(request.form['montoi_1000_CS'])
    token['montos_1_CS'] = float(request.form['montos_1_CS'])
    token['montos_5_CS'] = float(request.form['montos_5_CS'])
    token['montos_10_CS'] = float(request.form['montos_10_CS'])
    token['montos_20_CS'] = float(request.form['montos_20_CS'])
    token['montos_50_CS'] = float(request.form['montos_50_CS'])
    token['montos_100_CS'] = float(request.form['montos_100_CS'])
    token['montos_200_CS'] = float(request.form['montos_200_CS'])
    token['montos_500_CS'] = float(request.form['montos_500_CS'])
    token['montos_1000_CS'] = float(request.form['montos_1000_CS'])
    token['montoi_1_US'] = float(request.form['montoi_1_US'])
    token['montoi_5_US'] = float(request.form['montoi_5_US'])
    token['montoi_10_US'] = float(request.form['montoi_10_US'])
    token['montoi_20_US'] = float(request.form['montoi_20_US'])
    token['montoi_50_US'] = float(request.form['montoi_50_US'])
    token['montoi_100_US'] = float(request.form['montoi_100_US'])
    token['montos_1_US'] = float(request.form['montos_1_US'])
    token['montos_5_US'] = float(request.form['montos_5_US'])
    token['montos_10_US'] = float(request.form['montos_10_US'])
    token['montos_20_US'] = float(request.form['montos_20_US'])
    token['montos_50_US'] = float(request.form['montos_50_US'])
    token['montos_100_US'] = float(request.form['montos_100_US'])
    return token
    