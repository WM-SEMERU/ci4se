def reset_and_halt(self, reset_type=None):
    delegateResult = self.call_delegate('set_reset_catch', core=self,
        reset_type=reset_type)
    if not delegateResult:
        self.halt()
    demcr = self.read_memory(CortexM.DEMCR)
    if not delegateResult:
        self.write_memory(CortexM.DEMCR, demcr | CortexM.DEMCR_VC_CORERESET)
    self.reset(reset_type)
    with timeout.Timeout(2.0) as t_o:
        while t_o.check():
            if self.get_state() not in (Target.TARGET_RESET, Target.
                TARGET_RUNNING):
                break
            sleep(0.01)
    xpsr = self.read_core_register('xpsr')
    if xpsr & self.XPSR_THUMB == 0:
        self.write_core_register('xpsr', xpsr | self.XPSR_THUMB)
    self.call_delegate('clear_reset_catch', core=self, reset_type=reset_type)
    self.write_memory(CortexM.DEMCR, demcr)