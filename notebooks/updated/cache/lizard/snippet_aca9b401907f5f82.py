def setpathcost(self, port, cost):
    _runshell([brctlexe, 'setpathcost', self.name, port, str(cost)], 
        'Could not set path cost in port %s in %s.' % (port, self.name))