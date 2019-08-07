from models.shared import db


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column('idPedido', db.Integer, db.ForeignKey("Pedido.idPedido"))
    subTotal = db.Column(db.float)
    idMedicamento = db.Column('idMedicamento', db.Integer, db.ForeignKey("Medicamento.idMedicamento"))

    def __init__(self, idPedido, idMedicamento):
        self.idPedido = idPedido
        self.idMedicamento = idMedicamento

    def __repr__(self):
        return ''
