def fix_engine_table(cls):
    if cls.engine.table_name:
        return
    storage_models = [b for b in cls.__bases__ if issubclass(b, Model) and 
        not issubclass(b, DistributedModel)]
    if not storage_models:
        raise TypeError(
            'When defining Distributed engine without the table_name ensure that your model has a parent model'
            )
    if len(storage_models) > 1:
        raise TypeError(
            'When defining Distributed engine without the table_name ensure that your model has exactly one non-distributed superclass'
            )
    cls.engine.table = storage_models[0]