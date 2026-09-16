def split_name(name):
    given1, _, rem = name.partition('/')
    surname, _, given2 = rem.partition('/')
    return given1.strip(), surname.strip(), given2.strip()