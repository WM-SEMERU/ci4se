def started(self, component):
    self.log('Running.')
    self.log('Started event origin: ', component, lvl=verbose)
    populate_user_events()
    from hfos.events.system import AuthorizedEvents
    self.log(len(AuthorizedEvents), 'authorized event sources:', list(
        AuthorizedEvents.keys()), lvl=debug)
    self._instantiate_components()
    self._start_frontend()
    self.fire(ready(), 'hfosweb')