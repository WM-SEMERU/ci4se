def SendDatagram(self, Text, Streams=None):
    if Streams is None:
        Streams = self.Streams
    for s in Streams:
        s.SendDatagram(Text)