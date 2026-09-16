def init(self, bootstrap_with):
    formula = WCNF()
    for to_hit in bootstrap_with:
        to_hit = list(map(lambda obj: self.idpool.id(obj), to_hit))
        formula.append(to_hit)
    for obj_id in six.iterkeys(self.idpool.id2obj):
        formula.append([-obj_id], weight=1)
    if self.htype == 'rc2':
        self.oracle = RC2(formula, solver=self.solver, adapt=False, exhaust
            =True, trim=5)
    elif self.htype == 'lbx':
        self.oracle = LBX(formula, solver_name=self.solver, use_cld=True)
    else:
        self.oracle = MCSls(formula, solver_name=self.solver, use_cld=True)