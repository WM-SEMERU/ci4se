def _SetPacketSizeForFollowingConnections(cursor):
    cur_packet_size = int(_ReadVariable('max_allowed_packet', cursor))
    if cur_packet_size < MAX_PACKET_SIZE:
        logging.warning(
            'MySQL max_allowed_packet of %d is required, got %d. Overwriting.',
            MAX_PACKET_SIZE, cur_packet_size)
        _SetGlobalVariable('max_allowed_packet', MAX_PACKET_SIZE, cursor)