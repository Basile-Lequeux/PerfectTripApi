from app import db
from sqlalchemy.dialects.postgresql import UUID

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
                )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('posts', lazy=True))

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'))
    created_by = db.relationship('User', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y')),
            "tags": self.tags_to_dict(),
            "created_by": self.created_by
        }

    def tags_to_dict(self):
        array = []
        for tag in self.tags:
            array.append(tag.name)
        return array


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
