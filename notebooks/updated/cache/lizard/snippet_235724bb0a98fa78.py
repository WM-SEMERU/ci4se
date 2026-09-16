def find_best_plan(self):
    for plan in self.plans:
        for strat in self.strategy:
            self.run_plan(plan, strat)