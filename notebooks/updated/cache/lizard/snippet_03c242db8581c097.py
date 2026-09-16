def calc_v_qa_v1(self):
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    aid = self.sequences.aides.fastaccess
    aid.qa = min(aid.qa, flu.qz + der.nmbsubsteps / der.seconds * aid.v)
    aid.v = max(aid.v + der.seconds / der.nmbsubsteps * (flu.qz - aid.qa), 0.0)