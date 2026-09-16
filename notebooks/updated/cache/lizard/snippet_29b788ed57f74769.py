def by_name(cls, session, name):
    pkg = cls.first(session, where=(cls.name.like(name),))
    if not pkg:
        name = name.replace('-', '_').upper()
        pkg = cls.first(session, where=(cls.name.like(name),))
        if pkg and pkg.name.upper().replace('-', '_') != name:
            pkg = None
    return pkg