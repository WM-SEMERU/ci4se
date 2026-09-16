def process_packet(self, pkt):
    if not (self.mode & ScannerMode.MODE_IBEACON and pkt[19:23] ==
        b'L\x00\x02\x15' or self.mode & ScannerMode.MODE_EDDYSTONE and pkt[
        19:21] == b'\xaa\xfe' or self.mode & ScannerMode.MODE_ESTIMOTE and 
        pkt[19:21] == b'\x9a\xfe'):
        return
    bt_addr = bt_addr_to_string(pkt[7:13])
    rssi = bin_to_int(pkt[-1])
    packet = parse_packet(pkt[14:-1])
    if not packet:
        return
    self.save_bt_addr(packet, bt_addr)
    properties = self.get_properties(packet, bt_addr)
    if self.device_filter is None and self.packet_filter is None:
        self.callback(bt_addr, rssi, packet, properties)
    elif self.device_filter is None:
        if is_one_of(packet, self.packet_filter):
            self.callback(bt_addr, rssi, packet, properties)
    else:
        if self.packet_filter and not is_one_of(packet, self.packet_filter):
            return
        for filtr in self.device_filter:
            if isinstance(filtr, BtAddrFilter):
                if filtr.matches({'bt_addr': bt_addr}):
                    self.callback(bt_addr, rssi, packet, properties)
                    return
            elif filtr.matches(properties):
                self.callback(bt_addr, rssi, packet, properties)
                return