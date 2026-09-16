def get_or_create_index(cls, app, wh):
    if wh in app.extensions['whooshee']['whoosheers_indexes']:
        return app.extensions['whooshee']['whoosheers_indexes'][wh]
    index = cls.create_index(app, wh)
    app.extensions['whooshee']['whoosheers_indexes'][wh] = index
    return index