def make_cidr(gw, mask):
    try:
        int_mask = 4294967295 << 32 - int(mask) & 4294967295
        gw_addr_int = struct.unpack('>L', socket.inet_aton(gw))[0] & int_mask
        return socket.inet_ntoa(struct.pack('!I', gw_addr_int)) + '/' + str(
            mask)
    except (socket.error, struct.error, ValueError, TypeError):
        return