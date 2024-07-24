from app.extensions import db
# transaccion
# tipo_operacion
# montotrus
# montopus
# montotrcs
# montopcs
#clase de operaciones Western Union
class OpWu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_operacion = db.Column(db.String(50), nullable=False)
    codigo_mtcn = db.Column(db.String(50), nullable=False)
    transaccion = db.Column(db.String(50), nullable=False)
    montotrus = db.Column(db.Float, nullable=False)
    montopus = db.Column(db.Float, nullable=False)
    montotrcs = db.Column(db.Float, nullable=False)
    montopcs = db.Column(db.Float, nullable=False)
