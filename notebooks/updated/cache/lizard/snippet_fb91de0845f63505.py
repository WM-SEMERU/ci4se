def lexicase(self, F, num_selections=None, survival=False):
    if num_selections is None:
        num_selections = F.shape[0]
    winners = []
    locs = []
    individual_locs = np.arange(F.shape[0])
    for i in np.arange(num_selections):
        can_locs = individual_locs
        cases = list(np.arange(F.shape[1]))
        self.random_state.shuffle(cases)
        while len(cases) > 0 and len(can_locs) > 1:
            best_val_for_case = np.min(F[can_locs, cases[0]])
            can_locs = [l for l in can_locs if F[l, cases[0]] <=
                best_val_for_case]
            cases.pop(0)
        choice = self.random_state.randint(len(can_locs))
        locs.append(can_locs[choice])
        if survival:
            individual_locs = [i for i in individual_locs if i != can_locs[
                choice]]
    while len(locs) < num_selections:
        locs.append(individual_locs[0])
    return locs