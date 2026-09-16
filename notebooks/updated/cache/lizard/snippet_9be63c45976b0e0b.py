def initialize(self, givengraph, sfa=False):
    sm_vector, smi_vector, em_vector = self._init_using_k_equivalence(
        givengraph, sfa)
    return sm_vector, smi_vector, em_vector