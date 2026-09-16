def run(self, iterator, play_context, result=0):
    ansible_mitogen.process.MuxProcess.start()
    run = super(StrategyMixin, self).run
    self._add_plugin_paths()
    self._install_wrappers()
    try:
        return mitogen.core._profile_hook('Strategy', lambda : run(iterator,
            play_context))
    finally:
        self._remove_wrappers()