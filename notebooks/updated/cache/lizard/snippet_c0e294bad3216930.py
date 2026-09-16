def load_calibration(self):
    registers = self.i2c_read_register(170, 22)
    self.cal['AC1'], self.cal['AC2'], self.cal['AC3'], self.cal['AC4'
        ], self.cal['AC5'], self.cal['AC6'], self.cal['B1'], self.cal['B2'
        ], self.cal['MB'], self.cal['MC'], self.cal['MD'] = struct.unpack(
        '>hhhHHHhhhhh', registers)