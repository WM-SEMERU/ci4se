def write(self, data):
    report_size = self.packet_size
    if self.ep_out:
        report_size = self.ep_out.wMaxPacketSize
    for _ in range(report_size - len(data)):
        data.append(0)
    self.read_sem.release()
    self.ep_out.write(data)