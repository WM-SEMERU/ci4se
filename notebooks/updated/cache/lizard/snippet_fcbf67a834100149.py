def execute(self, program: Program):
    for dg in program.defined_gates:
        if dg.parameters is not None:
            raise NotImplementedError(
                'PyQVM does not support parameterized DEFGATEs')
        self.defined_gates[dg.name] = dg.matrix
    self.program = program
    self.program_counter = 0
    halted = len(program) == 0
    while not halted:
        halted = self.transition()
    return self