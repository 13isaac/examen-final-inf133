from app.database import db
from datetime import date
class Reserva(db.Model):
    __tablenam__ = "reservas"

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, nullable=False, unique=True)
    restaurante_id=db.Column(db.Integer, nullable=False)
    reservation_date=db.Column(db.Date, nullable=False)
    num_guests=db.Column(db.Integer, nullable=False)
    special_requests=db.Column(db.String(50), nullable=False)
    status=db.Column(db.String(50), nullable=False)

    def __init__(self,user_id,restaurante_id,reservation_date,num_guests,special_requests,status):
        self.user_id=int(user_id)
        self.restaurante_id=int(restaurante_id)
        f=list(reservation_date.split("-"))
        año=int(f[0])
        mes=int(f[1])
        dia=int(f[2][0]+f[2][1])
        fecha=date(año,mes,dia)
        self.reservation_date=fecha
        self.num_guests=int(num_guests)
        self.special_requests=special_requests
        self.status=status

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,user_id=None,restaurante_id=None,reservation_date=None,num_guests=None,special_requests=None,status=None):
        if user_id is not None:
            self.user_id=int(user_id)
        if restaurante_id is not None:
            self.restaurante_id=int(restaurante_id)
        if reservation_date is not None:
            f=list(reservation_date.split("-"))
            año=int(f[0])
            mes=int(f[1])
            dia=int(f[2][0]+f[2][1])
            fecha=date(año,mes,dia)
            self.reservation_date=fecha
        if num_guests is not None:
            self.num_guests=int(num_guests)
        if special_requests is not None:
            self.special_requests=special_requests
        if status is not None:
            self.status=status
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Reserva.query.get(id)
    
    @staticmethod
    def get_all():
        return Reserva.query.all()
    
