def filter_cols(model, *filtered_columns):
    m = sa.orm.class_mapper(model)
    return list({p.key for p in m.iterate_properties if hasattr(p,
        'columns')}.difference(filtered_columns))