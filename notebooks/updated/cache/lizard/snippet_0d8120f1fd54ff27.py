def commit(self):
    self.query.globl['branch'] = self._obranch
    self.query.globl['turn'] = self._oturn
    self.query.globl['tick'] = self._otick
    set_branch = self.query.set_branch
    for branch, (parent, turn_start, tick_start, turn_end, tick_end
        ) in self._branches.items():
        set_branch(branch, parent, turn_start, tick_start, turn_end, tick_end)
    turn_end = self._turn_end
    set_turn = self.query.set_turn
    for (branch, turn), plan_end_tick in self._turn_end_plan.items():
        set_turn(branch, turn, turn_end[branch], plan_end_tick)
    if self._plans_uncommitted:
        self.query.plans_insert_many(self._plans_uncommitted)
    if self._plan_ticks_uncommitted:
        self.query.plan_ticks_insert_many(self._plan_ticks_uncommitted)
    self.query.commit()
    self._plans_uncommitted = []
    self._plan_ticks_uncommitted = []