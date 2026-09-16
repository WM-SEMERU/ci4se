def set_pattern_step_time(self, patternnumber, stepnumber, timevalue):
    _checkPatternNumber(patternnumber)
    _checkStepNumber(stepnumber)
    _checkTimeValue(timevalue, self.time_max)
    address = _calculateRegisterAddress('time', patternnumber, stepnumber)
    self.write_register(address, timevalue, 0)