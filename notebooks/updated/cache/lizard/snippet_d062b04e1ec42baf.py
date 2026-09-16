def escape_dictionary(dictionary, datetime_format='%Y-%m-%d %H:%M:%S'):
    for k, v in dictionary.iteritems():
        if isinstance(v, datetime.datetime):
            v = v.strftime(datetime_format)
        if isinstance(v, basestring):
            v = CoyoteDb.db_escape(str(v))
            v = '"{}"'.format(v)
        if v is True:
            v = 1
        if v is False:
            v = 0
        if v is None:
            v = 'NULL'
        dictionary[k] = v