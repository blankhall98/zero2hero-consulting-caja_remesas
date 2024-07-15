from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class CajaForm(FlaskForm):
    #moneda local
    moneda_local_1 = IntegerField('1 Córdoba', validators=[DataRequired()])
    moneda_local_5 = IntegerField('5 Córdobas', validators=[DataRequired()])
    moneda_local_10 = IntegerField('10 Córdobas', validators=[DataRequired()])
    moneda_local_20 = IntegerField('20 Córdobas', validators=[DataRequired()])
    moneda_local_50 = IntegerField('50 Córdobas', validators=[DataRequired()])
    moneda_local_100 = IntegerField('100 Córdobas', validators=[DataRequired()])
    moneda_local_200 = IntegerField('200 Córdobas', validators=[DataRequired()])
    moneda_local_500 = IntegerField('500 Córdobas', validators=[DataRequired()])
    moneda_local_1000 = IntegerField('1000 Córdobas', validators=[DataRequired()])

    #moneda dolar
    dolar_1 = IntegerField('1 Dólar', validators=[DataRequired()])
    dolar_5 = IntegerField('5 Dólares', validators=[DataRequired()])
    dolar_10 = IntegerField('10 Dólares', validators=[DataRequired()])
    dolar_20 = IntegerField('20 Dólares', validators=[DataRequired()])
    dolar_50 = IntegerField('50 Dólares', validators=[DataRequired()])
    dolar_100 = IntegerField('100 Dólares', validators=[DataRequired()])
    # entregar
    submit = SubmitField('Actualizar Caja')