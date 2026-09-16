def get_by_email(cls, email):
    return cls.query().filter(cls.email == email).first()