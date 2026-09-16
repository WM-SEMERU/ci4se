def get_parameters(self, packet_count=None):
    params = super(LiveCapture, self).get_parameters(packet_count=packet_count)
    params += ['-r', '-']
    return params