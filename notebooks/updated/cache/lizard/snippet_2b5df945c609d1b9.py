def _one_to_many_query(cls, query_obj, search4, model_attrib):
    model = model_attrib.parent.class_
    already_joined_tables = [mapper.class_ for mapper in query_obj.
        _join_entities]
    if isinstance(search4, (str, int, Iterable)
        ) and model not in already_joined_tables:
        query_obj = query_obj.join(model)
    if isinstance(search4, str):
        query_obj = query_obj.filter(model_attrib.like(search4))
    elif isinstance(search4, int):
        query_obj = query_obj.filter(model_attrib == search4)
    elif isinstance(search4, Iterable):
        query_obj = query_obj.filter(model_attrib.in_(search4))
    return query_obj