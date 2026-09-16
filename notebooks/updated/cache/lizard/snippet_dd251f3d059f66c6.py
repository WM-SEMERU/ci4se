def _translate_jcc(self, oprnd1, oprnd2, oprnd3):
    assert oprnd1.size and oprnd3.size
    op1_var = self._translate_src_oprnd(oprnd1)
    return [op1_var != 0]