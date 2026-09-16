def get(cls, dname):
    Domain = cls
    dname = dname.hostname if hasattr(dname, 'hostname') else dname.lower()
    return Session.query(Domain).filter(Domain.name == dname).first()