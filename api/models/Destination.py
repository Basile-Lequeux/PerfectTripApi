import json
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


def add_destinations_to_db():
    with open('cities.json') as file:
        content = file.read()
        document = json.loads(content)
        for line in document:
            city = line['Ville']
            country = line['pays']
            destination = Destination(name=city, country=country)
            db.session.add(destination)

        file.close()
        db.session.commit()