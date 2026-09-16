def source_addr_mode2(pkt):
    if pkt.sac == 0:
        if pkt.sam == 0:
            return 16
        elif pkt.sam == 1:
            return 8
        elif pkt.sam == 2:
            return 2
        elif pkt.sam == 3:
            return 0
    elif pkt.sam == 0:
        return 0
    elif pkt.sam == 1:
        return 8
    elif pkt.sam == 2:
        return 2
    elif pkt.sam == 3:
        return 0