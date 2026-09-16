def _instantiate_components(self, clear=True):
    if clear:
        import objgraph
        from copy import deepcopy
        from circuits.tools import kill
        from circuits import Component
        for comp in self.runningcomponents.values():
            self.log(comp, type(comp), isinstance(comp, Component), pretty=True
                )
            kill(comp)
        self.runningcomponents = {}
    self.log('Not running blacklisted components: ', self.
        component_blacklist, lvl=debug)
    running = set(self.loadable_components.keys()).difference(self.
        component_blacklist)
    self.log('Starting components: ', sorted(running))
    for name, componentdata in self.loadable_components.items():
        if name in self.component_blacklist:
            continue
        self.log('Running component: ', name, lvl=verbose)
        try:
            if name in self.runningcomponents:
                self.log('Component already running: ', name, lvl=warn)
            else:
                runningcomponent = componentdata()
                runningcomponent.register(self)
                self.runningcomponents[name] = runningcomponent
        except Exception as e:
            self.log('Could not register component: ', name, e, type(e),
                lvl=error, exc=True)