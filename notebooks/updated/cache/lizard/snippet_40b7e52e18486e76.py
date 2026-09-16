def _packet_ack(self, packet, sequence):
    if packet['sequence'] == sequence:
        if packet['payloadtype'] == PayloadType.SETCOLOR:
            self._color_callback(packet['target'], packet['hue'], packet[
                'sat'], packet['bri'], packet['kel'])
        elif packet['payloadtype'] == PayloadType.SETPOWER2:
            self._power_callback(packet['target'], packet['power'])
        return False
    return True