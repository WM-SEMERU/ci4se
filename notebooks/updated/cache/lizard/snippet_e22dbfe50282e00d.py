def resources(self):
    return sa.orm.relationship('Resource', cascade='all', passive_deletes=
        True, passive_updates=True, backref='owner', lazy='dynamic')