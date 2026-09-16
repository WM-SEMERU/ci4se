def _gql(cls, query_string, *args, **kwds):
    from .query import gql
    return gql('SELECT * FROM %s %s' % (cls._class_name(), query_string), *
        args, **kwds)