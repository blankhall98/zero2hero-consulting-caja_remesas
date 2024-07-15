from app.extensions import db
from datetime import datetime

class Caja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # Moneda local
    moneda_local_1 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 1
    moneda_local_5 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 5
    moneda_local_10 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 10
    moneda_local_20 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 20
    moneda_local_50 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 50
    moneda_local_100 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 100
    moneda_local_200 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 200
    moneda_local_500 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 500
    moneda_local_1000 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 1000
    # Moneda dolar
    dolar_1 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 1 dólar
    dolar_5 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 5 dólares
    dolar_10 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 10 dólares
    dolar_20 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 20 dólares
    dolar_50 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 50 dólares
    dolar_100 = db.Column(db.Integer, default=0)  # Ejemplo: billetes de 100 dólares

    def __repr__(self):
        return f'<Caja {self.fecha}>'
