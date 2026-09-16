def generate_boosted_machine(self):
    strong = bob.learn.boosting.BoostedMachine()
    for machine, index in zip(self.cascade, self.indices):
        weak = machine.weak_machines
        weights = machine.weights
        for i in range(len(weak)):
            strong.add_weak_machine(weak[i], weights[i])
    return strong