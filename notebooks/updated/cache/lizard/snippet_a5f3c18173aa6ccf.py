def create(cls, name, trust_all_cas=True):
    json = {'name': name, 'trust_all_cas': trust_all_cas}
    return ElementCreator(cls, json)