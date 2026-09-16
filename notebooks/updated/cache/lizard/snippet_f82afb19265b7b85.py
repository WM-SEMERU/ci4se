def get_bulb(self, mac):
    return self.bulbs.get(mac, Bulb('Bulb %s' % _bytes(mac), mac))