def process(self, input_data, topic=None, **kwargs):
    try:
        split = input_data[1:-1].split(',', 1)
        uid, pkt = int(split[0]), split[1]
        defn = self.packet_dict[uid]
        decoded = tlm.Packet(defn, data=bytearray(pkt))
        self.dbconn.insert(decoded, **kwargs)
    except Exception as e:
        log.error('Data archival failed with error: {}.'.format(e))