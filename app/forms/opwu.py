from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

# transaccion
# tipo_operacion
# montotrus
# montopus
# montotrcs
# montopcs

class OpWuForm(FlaskForm):
    transaccion = SelectField('Transacción', choices=[
        ('pago_remesa_wu_us', 'Pago de Remesa WU US'),
        ('pago_remesa_wu_cs', 'Pago de Remesa WU CS'),
        ('envio_remesa_wu_us', 'Envio de Remesa WU US'),
        ('envio_remesa_wu_cs', 'Envio de Remesa WU CS')
    ], validators=[DataRequired()])
    tipo_operacion = SelectField('Tipo de Operación', choices=[
        ('egreso', 'Egreso'),
        ('ingreso', 'Ingreso')
    ], validators=[DataRequired()])
    montotrus = FloatField('Monto Transacción US')
    montopus = FloatField('Monto Pago US')
    montotrcs = FloatField('Monto Transacción CS')
    montopcs = FloatField('Monto Pago CS')
    
    montoi_1000_CS = FloatField('1000 CS')
    montoi_500_CS = FloatField('500 CS')
    montoi_200_CS = FloatField('200 CS')
    montoi_100_CS = FloatField('100 CS')
    montoi_50_CS = FloatField('50 CS')
    montoi_20_CS = FloatField('20 CS')
    montoi_10_CS = FloatField('10 CS')
    montoi_5_CS = FloatField('5 CS')
    montoi_1_CS = FloatField('1 CS')
    total_entradas_CS = FloatField('Total Entradas CS')
    cambioi_CS = FloatField('Cambio Inicial CS')
    montos_1000_CS = FloatField('1000 CS')
    montos_500_CS = FloatField('500 CS')
    montos_200_CS = FloatField('200 CS')
    montos_100_CS = FloatField('100 CS')
    montos_50_CS = FloatField('50 CS')
    montos_20_CS = FloatField('20 CS')
    montos_10_CS = FloatField('10 CS')
    montos_5_CS = FloatField('5 CS')
    montos_1_CS = FloatField('1 CS')
    total_Salidas_CS = FloatField('Total Salidas CS')
    ajuste_CS = FloatField('Ajuste CS')
    montoE_100_US = FloatField('100 US')
    montoE_50_US = FloatField('50 US')
    montoE_20_US = FloatField('20 US')
    montoE_10_US = FloatField('10 US')
    montoE_5_US = FloatField('5 US')
    montoE_1_US = FloatField('1 US')
    total_entradas_US = FloatField('Total Entradas US')
    cambioE_US = FloatField('Cambio Inicial US')
    montoP_100_US = FloatField('100 US')
    montoP_50_US = FloatField('50 US')
    montoP_20_US = FloatField('20 US')
    montoP_10_US = FloatField('10 US')
    montoP_5_US = FloatField('5 US')
    montoP_1_US = FloatField('1 US')
    total_salidas_US = FloatField('Total Salidas US')
    ajuste_US = FloatField('Ajuste US')
    ajuste = FloatField('Ajuste')
    submit = SubmitField('Guardar')