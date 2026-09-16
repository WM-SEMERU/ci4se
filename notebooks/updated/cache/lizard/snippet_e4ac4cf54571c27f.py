def add_msg(self, pkt):
    if not self.buffer_out:
        self.add_record()
    r = self.buffer_out[-1]
    if isinstance(r, TLS13):
        self.buffer_out[-1].inner.msg.append(pkt)
    else:
        self.buffer_out[-1].msg.append(pkt)