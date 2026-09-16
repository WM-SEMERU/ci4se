def send_simple_command(self, cmd):
    pkt = MqttPkt()
    pkt.command = cmd
    pkt.remaining_length = 0
    ret = pkt.alloc()
    if ret != NC.ERR_SUCCESS:
        return ret
    return self.packet_queue(pkt)