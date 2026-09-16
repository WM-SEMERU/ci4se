def get(self, conn_name, default=None, **kwargs):
    if isinstance(conn_name, RdfwConnections):
        return conn_name
    try:
        return self.conns[conn_name]
    except KeyError:
        if default:
            return self.get(default, **kwargs)
        raise LookupError("'%s' connection has not been set" % conn_name)