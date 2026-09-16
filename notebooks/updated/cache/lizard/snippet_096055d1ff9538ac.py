def raw_command(netfn, command, bridge_request=None, data=(), retry=True,
    delay_xmit=None, **kwargs):
    with _IpmiSession(**kwargs) as s:
        r = s.raw_command(netfn=int(netfn), command=int(command),
            bridge_request=bridge_request, data=data, retry=retry,
            delay_xmit=delay_xmit)
        return r