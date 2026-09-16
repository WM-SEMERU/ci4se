def v1(self):
    Vm = self.system.dae.y[self.v]
    Va = self.system.dae.y[self.a]
    return polar(Vm[self.a1], Va[self.a1])