def send_and_receive(self, req):
    rx_data = self._send_and_receive(target=req.target, lun=req.lun, netfn=
        req.netfn, cmdid=req.cmdid, payload=encode_message(req))
    rsp = create_message(req.netfn + 1, req.cmdid, req.group_extension)
    decode_message(rsp, rx_data)
    return rsp