def show(self, id):
    lt = meta.Session.query(LayerTemplate).get(id)
    if lt is None:
        abort(404)
    return lt.to_json()