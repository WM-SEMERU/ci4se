def candidate(cls):
    return relationship('Candidate', backref=backref(camel_to_under(cls.
        __name__) + 's', cascade='all, delete-orphan', cascade_backrefs=
        False), cascade_backrefs=False)