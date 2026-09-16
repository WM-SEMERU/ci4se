def save_kb_dyn_config(kb_id, field, expression, collection=None):
    if collection:
        collection = Collection.query.filter_by(name=collection).one()
    kb = get_kb_by_id(kb_id)
    kb.set_dyn_config(field, expression, collection)