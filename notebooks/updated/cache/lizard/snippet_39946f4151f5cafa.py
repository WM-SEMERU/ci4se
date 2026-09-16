def ipv4_reassembly(packet, *, count=NotImplemented):
    if 'IP' in packet:
        ipv4 = packet['IP']
        if ipv4.flags.DF:
            return False, None
        data = dict(bufid=(ipaddress.ip_address(ipv4.src), ipaddress.
            ip_address(ipv4.dst), ipv4.id, TP_PROTO.get(ipv4.proto).name),
            num=count, fo=ipv4.frag, ihl=ipv4.ihl, mf=bool(ipv4.flags.MF),
            tl=ipv4.len, header=bytearray(ipv4.raw_packet_cache), payload=
            bytearray(bytes(ipv4.payload)))
        return True, data
    return False, None