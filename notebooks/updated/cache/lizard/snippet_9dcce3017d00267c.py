def goes_requires(self, regs):
    if len(self) and self.mem[-1].inst == 'call' and self.mem[-1
        ].condition_flag is None:
        for block in self.calls:
            if block.is_used(regs, 0):
                return True
            d = block.destroys()
            if not len([x for x in regs if x not in d]):
                return False
    for block in self.goes_to:
        if block.is_used(regs, 0):
            return True
    return False