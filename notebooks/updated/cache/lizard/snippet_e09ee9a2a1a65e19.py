def get_pk(obj):
    if inspect.isclass(obj):
        pk_list = sqlalchemy.inspect(obj).primary_key
    else:
        pk_list = obj.__mapper__.primary_key
    return pk_list