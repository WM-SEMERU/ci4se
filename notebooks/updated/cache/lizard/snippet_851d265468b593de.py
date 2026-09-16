def translate(self, by):
    new_positions = _translate(self.xyz_with_ports, by)
    self.xyz_with_ports = new_positions