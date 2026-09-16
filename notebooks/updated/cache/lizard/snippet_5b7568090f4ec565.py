def transitionStates(self, state):
    newstates, rates = self.transition(state)
    newindices = self.getStateIndex(newstates)
    return newindices, rates