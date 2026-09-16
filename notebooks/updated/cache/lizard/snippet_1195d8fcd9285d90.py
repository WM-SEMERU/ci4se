def defineBiophysics(self):
    self.soma.insert('hh')
    self.soma.gnabar_hh = 0.12
    self.soma.gkbar_hh = 0.036
    self.soma.gl_hh = 0.003
    self.soma.el_hh = -70
    self.dend.insert('pas')
    self.dend.g_pas = 0.001
    self.dend.e_pas = -65
    self.dend.nseg = 1000