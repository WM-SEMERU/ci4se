def Chemistry(self):
    length = self.bus.read_byte_data(self.address, 121)
    chem = []
    for n in range(length):
        chem.append(self.bus.read_byte_data(self.address, 122 + n))
    return chem