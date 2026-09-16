def needs_restart(self, option_fingerprint):
    should_shutdown_after_run = self._bootstrap_options.for_global_scope(
        ).shutdown_pantsd_after_run
    return super(PantsDaemon, self).needs_restart(option_fingerprint
        ) or self.is_alive() and should_shutdown_after_run