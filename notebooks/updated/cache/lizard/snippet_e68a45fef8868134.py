def add(self, classifier, threshold, begin=None, end=None):
    boosted_machine = bob.learn.boosting.BoostedMachine()
    if begin is None:
        begin = 0
    if end is None:
        end = len(classifier.weak_machines)
    for i in range(begin, end):
        boosted_machine.add_weak_machine(classifier.weak_machines[i],
            classifier.weights[i])
    self.cascade.append(boosted_machine)
    self.thresholds.append(threshold)
    self._indices()