def _nln_constraints(self, nb, nl):
    Pmis = NonLinearConstraint('Pmis', nb)
    Qmis = NonLinearConstraint('Qmis', nb)
    Sf = NonLinearConstraint('Sf', nl)
    St = NonLinearConstraint('St', nl)
    return Pmis, Qmis, Sf, St