from api import db


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def to_dict(self):
        return {
            "uuid": self.id,
            "email": self.name
        }
