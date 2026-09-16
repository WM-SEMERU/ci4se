def accessible(self, fromstate, tostate):
    if (not fromstate in self.nodes or not tostate in self.nodes or not 
        fromstate in self.edges_out):
        return 0
    if tostate in self.edges_out[fromstate]:
        return self.edges_out[fromstate][tostate]
    else:
        return 0