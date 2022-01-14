from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from sqlalchemy_utils.types.password import PasswordType


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
