def submit_rpc(self, rpc_name, params, flags=0):
    logger.info('Sending RPC %s flags=%d', rpc_name, flags)
    self.messages = []
    self.output_params = {}
    self.cancel_if_pending()
    self.res_info = None
    w = self._writer
    with self.querying_context(tds_base.PacketType.RPC):
        if tds_base.IS_TDS72_PLUS(self):
            self._start_query()
        if tds_base.IS_TDS71_PLUS(self) and isinstance(rpc_name, tds_base.
            InternalProc):
            w.put_smallint(-1)
            w.put_smallint(rpc_name.proc_id)
        else:
            if isinstance(rpc_name, tds_base.InternalProc):
                rpc_name = rpc_name.name
            w.put_smallint(len(rpc_name))
            w.write_ucs2(rpc_name)
        w.put_usmallint(flags)
        self._out_params_indexes = []
        for i, param in enumerate(params):
            if param.flags & tds_base.fByRefValue:
                self._out_params_indexes.append(i)
            w.put_byte(len(param.column_name))
            w.write_ucs2(param.column_name)
            w.put_byte(param.flags)
            serializer = param.choose_serializer(type_factory=self._tds.
                type_factory, collation=self._tds.collation or raw_collation)
            type_id = serializer.type
            w.put_byte(type_id)
            serializer.write_info(w)
            serializer.write(w, param.value)