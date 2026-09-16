def _list_collections(self, sock_info, slave_okay, session, read_preference,
    **kwargs):
    coll = self.get_collection('$cmd', read_preference=read_preference)
    if sock_info.max_wire_version > 2:
        cmd = SON([('listCollections', 1), ('cursor', {})])
        cmd.update(kwargs)
        with self.__client._tmp_session(session, close=False) as tmp_session:
            cursor = self._command(sock_info, cmd, slave_okay,
                read_preference=read_preference, session=tmp_session)['cursor']
            return CommandCursor(coll, cursor, sock_info.address, session=
                tmp_session, explicit_session=session is not None)
    else:
        match = _INDEX_REGEX
        if 'filter' in kwargs:
            match = {'$and': [_INDEX_REGEX, kwargs['filter']]}
        dblen = len(self.name.encode('utf8') + b'.')
        pipeline = [{'$project': {'name': {'$substr': ['$name', dblen, -1]},
            'options': 1}}, {'$match': match}]
        cmd = SON([('aggregate', 'system.namespaces'), ('pipeline',
            pipeline), ('cursor', kwargs.get('cursor', {}))])
        cursor = self._command(sock_info, cmd, slave_okay)['cursor']
        return CommandCursor(coll, cursor, sock_info.address)