from api import db


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country
        }
