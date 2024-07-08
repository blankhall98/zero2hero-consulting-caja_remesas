from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

class TasaForm(FlaskForm):
    fecha = DateField('Fecha', format='%d-%m-%Y', default=datetime.utcnow, validators=[DataRequired()])
    tasa_oficial = FloatField('Tasa Oficial', validators=[DataRequired()])
    tasa_compra = FloatField('Tasa Compra', validators=[DataRequired()])
    tasa_venta = FloatField('Tasa Venta', validators=[DataRequired()])
    tasa_wu = FloatField('Tasa WU', validators=[DataRequired()])
    submit = SubmitField('Submit')