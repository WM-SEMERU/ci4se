def _write_packet(self, packet, sec=None, usec=None, caplen=None, wirelen=None
    ):
    if hasattr(packet, 'time'):
        if sec is None:
            sec = int(packet.time)
            usec = int(round((packet.time - sec) * (1000000000 if self.nano
                 else 1000000)))
    if usec is None:
        usec = 0
    rawpkt = raw(packet)
    caplen = len(rawpkt) if caplen is None else caplen
    if wirelen is None:
        if hasattr(packet, 'wirelen'):
            wirelen = packet.wirelen
    if wirelen is None:
        wirelen = caplen
    RawPcapWriter._write_packet(self, rawpkt, sec=sec, usec=usec, caplen=
        caplen, wirelen=wirelen)