def _fit_radec(self):
    self.orbfit.fitradec.restype = ctypes.c_int
    self.orbfit.fitradec.argtypes = [ctypes.c_char_p, ctypes.c_char_p,
        ctypes.c_char_p]
    mpc_file = tempfile.NamedTemporaryFile(suffix='.mpc')
    for observation in self.observations:
        mpc_file.write('{}\n'.format(str(observation)))
    mpc_file.seek(0)
    abg_file = tempfile.NamedTemporaryFile()
    res_file = tempfile.NamedTemporaryFile()
    self.orbfit.fitradec(ctypes.c_char_p(mpc_file.name), ctypes.c_char_p(
        abg_file.name), ctypes.c_char_p(res_file.name))
    self.abg = abg_file
    self.abg.seek(0)
    self.residuals = res_file
    self.residuals.seek(0)