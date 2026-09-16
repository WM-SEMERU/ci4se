def set_output(self, state, channel=2):
    if state:
        self.instr.write(':OUTP{0} ON'.format(channel))
    else:
        self.instr.write(':OUTP{0} OFF'.format(channel))