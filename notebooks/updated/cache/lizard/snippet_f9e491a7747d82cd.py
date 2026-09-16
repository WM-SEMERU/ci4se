def nvrtcGetProgramLog(self, prog):
    size = c_size_t()
    code = self._lib.nvrtcGetProgramLogSize(prog, byref(size))
    self._throw_on_error(code)
    buf = create_string_buffer(size.value)
    code = self._lib.nvrtcGetProgramLog(prog, buf)
    self._throw_on_error(code)
    return buf.value.decode('utf-8')