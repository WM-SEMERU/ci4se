def prop_budget(self, budget):
    if self.glucose:
        pysolvers.glucose3_pbudget(self.glucose, budget)