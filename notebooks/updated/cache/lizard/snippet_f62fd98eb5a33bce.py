def makeResetPacket(ID, param):
    if param not in [1, 2, 255]:
        raise Exception('Packet.makeResetPacket invalide parameter {}'.
            format(param))
    pkt = makePacket(ID, xl320.XL320_RESET, None, [1])
    return pkt