def distb(self, tb=None, file=None):
    if tb is None:
        try:
            tb = sys.last_traceback
        except AttributeError:
            raise RuntimeError('no last traceback to disassemble')
        while tb.tb_next:
            tb = tb.tb_next
    self.disassemble(tb.tb_frame.f_code, tb.tb_lasti, file=file)