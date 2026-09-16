def _can_callback(self, irs):
    for ir in irs:
        if isinstance(ir, LowLevelCall):
            return True
        if isinstance(ir, HighLevelCall) and not isinstance(ir, LibraryCall):
            if (self.slither.solc_version and self.slither.solc_version.
                startswith('0.5.')):
                if isinstance(ir.function, Function) and (ir.function.view or
                    ir.function.pure):
                    continue
                if isinstance(ir.function, Variable):
                    continue
            if ir.destination == SolidityVariable('this'):
                if isinstance(ir.function, Variable):
                    continue
                if not ir.function.all_high_level_calls():
                    if not ir.function.all_low_level_calls():
                        continue
            return True
    return False