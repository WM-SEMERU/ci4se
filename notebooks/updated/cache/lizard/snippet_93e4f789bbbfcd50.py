def add_trigger(self, trigger):
    self.sorted = False
    if trigger.priority not in self._triggers:
        self._triggers[trigger.priority] = [trigger]
        return
    self._triggers[trigger.priority].append(trigger)