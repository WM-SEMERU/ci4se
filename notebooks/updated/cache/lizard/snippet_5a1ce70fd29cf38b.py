def packets(self):
    if not self.get_object_by_type('cappacket'):
        for index in range(0, self.read_stats()['packets']):
            XenaCapturePacket(parent=self, index='{}/{}'.format(self.index,
                index))
    return {p.id: p for p in self.get_objects_by_type('cappacket')}