def revert(self):
    if self.program_fp:
        self.program_fp.close()
    super(ProgramRunner, self).revert()