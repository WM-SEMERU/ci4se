def map_reduce(self, map, reduce, out, full_response=False, **kwargs):
    if not isinstance(out, (string_type, collections.Mapping)):
        raise TypeError("'out' must be an instance of %s or a mapping" % (
            string_type.__name__,))
    cmd = SON([('mapreduce', self.__name), ('map', map), ('reduce', reduce),
        ('out', out)])
    collation = validate_collation_or_none(kwargs.pop('collation', None))
    cmd.update(kwargs)
    inline = 'inline' in cmd['out']
    with self._socket_for_primary_reads() as (sock_info, slave_ok):
        if (sock_info.max_wire_version >= 5 and self.write_concern and not
            inline):
            cmd['writeConcern'] = self.write_concern.document
        cmd.update(kwargs)
        if (sock_info.max_wire_version >= 4 and 'readConcern' not in cmd and
            inline):
            response = self._command(sock_info, cmd, slave_ok,
                ReadPreference.PRIMARY, read_concern=self.read_concern,
                collation=collation)
        else:
            response = self._command(sock_info, cmd, slave_ok,
                ReadPreference.PRIMARY, parse_write_concern_error=not
                inline, collation=collation)
    if full_response or not response.get('result'):
        return response
    elif isinstance(response['result'], dict):
        dbase = response['result']['db']
        coll = response['result']['collection']
        return self.__database.client[dbase][coll]
    else:
        return self.__database[response['result']]