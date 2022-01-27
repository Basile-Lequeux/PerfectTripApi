from api import db

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('destination_id', db.Integer, db.ForeignKey('destination.id'), primary_key=True)
                )


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(150), nullable=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('destinations', lazy=True))

    def to_dict(self):
        return {
            "uuid": self.id,
            "name": self.name,
            "tags": self.tags
        }


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
