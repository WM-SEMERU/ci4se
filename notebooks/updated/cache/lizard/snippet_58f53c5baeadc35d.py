def _handle_tag_fileattributes(self):
    obj = _make_object('FileAttributes')
    bc = BitConsumer(self._src)
    bc.u_get(1)
    obj.UseDirectBlit = bc.u_get(1)
    obj.UseGPU = bc.u_get(1)
    obj.HasMetadata = bc.u_get(1)
    obj.ActionScript3 = bc.u_get(1)
    bc.u_get(2)
    obj.UseNetwork = bc.u_get(1)
    bc.u_get(24)
    return obj