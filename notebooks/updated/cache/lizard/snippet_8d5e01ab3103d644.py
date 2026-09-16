def conf_budget(self, budget):
    if self.minisat:
        pysolvers.minisat22_cbudget(self.minisat, budget)