def tcp_reassembly(packet, *, count=NotImplemented):
    if 'TCP' in packet:
        ip = packet['IP'] if 'IP' in packet else packet['IPv6']
        tcp = packet['TCP']
        data = dict(bufid=(ipaddress.ip_address(ip.src), ipaddress.
            ip_address(ip.dst), tcp.sport, tcp.dport), num=count, ack=tcp.
            ack, dsn=tcp.seq, syn=bool(tcp.flags.S), fin=bool(tcp.flags.F),
            rst=bool(tcp.flags.R), payload=bytearray(bytes(tcp.payload)))
        raw_len = len(tcp.payload)
        data['first'] = tcp.seq
        data['last'] = tcp.seq + raw_len
        data['len'] = raw_len
        return True, data
    return False, None