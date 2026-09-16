def createSynapses(self):
    synsoma = h.ExpSyn(self.soma(0.5))
    synsoma.tau = 2
    synsoma.e = 0
    syndend = h.ExpSyn(self.dend(0.5))
    syndend.tau = 2
    syndend.e = 0
    self.synlist.append(synsoma)
    self.synlist.append(syndend)