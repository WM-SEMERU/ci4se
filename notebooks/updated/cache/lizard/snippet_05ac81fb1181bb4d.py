def at(self, step):
    return TimeMachine(self.uid, step=step, info=copy.deepcopy(self.info))