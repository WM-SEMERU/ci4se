def unfix_parameters(self):
    for W, b in zip(self.W_list, self.b_list):
        W.unfix()
        b.unfix()