def recv_func(self, rsp_pb, proto_id):
    if self.cb_check_recv is not None and not self.cb_check_recv(
        ) and ProtoId.is_proto_id_push(proto_id):
        return
    handler = self._default_handler
    pre_handler = None
    if proto_id in self._handler_table:
        handler = self._handler_table[proto_id]['obj']
    if proto_id in self._pre_handler_table:
        pre_handler = self._pre_handler_table[proto_id]['obj']
    if pre_handler is not None:
        pre_handler.on_recv_rsp(rsp_pb)
    handler.on_recv_rsp(rsp_pb)