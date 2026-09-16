def BLX(self, params):
    Rj = self.get_one_parameter(self.ONE_PARAMETER, params)
    self.check_arguments(LR_or_general_purpose_registers=(Rj,))

    def BLX_func():
        self.register['LR'] = self.register['PC']
        self.register['PC'] = self.register[Rj]
    return BLX_func