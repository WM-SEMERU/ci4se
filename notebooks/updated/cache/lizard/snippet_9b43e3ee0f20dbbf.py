def setup(db_class, simple_object_cls, primary_keys):
    table_name = simple_object_cls.__name__
    column_names = simple_object_cls.FIELDS
    metadata = MetaData()
    table = Table(table_name, metadata, *[Column(cname,
        _get_best_column_type(cname), primary_key=cname in primary_keys) for
        cname in column_names])
    db_class.metadata = metadata
    db_class.mapper_class = simple_object_cls
    db_class.table = table
    mapper(simple_object_cls, table)