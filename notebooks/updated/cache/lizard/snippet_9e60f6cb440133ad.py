def is_legal_priority(self, packet: DataPacket):
    if packet.universe not in self.callbacks.keys(
        ) or packet.priority < self.priorities[packet.universe][0]:
        return False
    else:
        return True