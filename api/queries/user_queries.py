from api.models.User import User


def login_resolver(obj, info, email, password):
    user = User.query.filter_by(email=email).first()
    print("password", user.password)
    if user.password == password:
        return True
    else:
        return False
