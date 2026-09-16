def set_checksum(self):
    data_sum = self.cmd1 + self.cmd2
    for i in range(1, 14):
        data_sum += self._userdata['d{:d}'.format(i)]
    chksum = 255 - (data_sum & 255) + 1
    self._userdata['d14'] = chksum