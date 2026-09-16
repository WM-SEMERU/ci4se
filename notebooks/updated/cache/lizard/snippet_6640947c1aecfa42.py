def setMode(self, mode, polarity, den, iovalue, data_length, reference,
    input_range, clock_enable, burn_out, channel):
    mode_MSB = (mode << 5) + (polarity << 4) + (den << 3) + (iovalue << 1
        ) + data_length
    mode_LSB = (reference << 7) + (0 << 6) + (input_range << 4) + (clock_enable
         << 3) + (burn_out << 2) + channel
    self.single_write(self.AD7730_MODE_REG, [mode_MSB, mode_LSB])