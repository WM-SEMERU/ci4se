def mysummary(self):
    if isinstance(self.underlayer, IP):
        return self.underlayer.sprintf(
            'IGMPv3: %IP.src% > %IP.dst% %IGMPv3.type% %IGMPv3.gaddr%')
    else:
        return self.sprintf('IGMPv3 %IGMPv3.type% %IGMPv3.gaddr%')