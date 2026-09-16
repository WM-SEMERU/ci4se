def getObjectives(self):
    objectives = lock_and_call(lambda : self._impl.getObjectives(), self._lock)
    return EntityMap(objectives, Objective)