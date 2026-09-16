def do_denyrep(self, line):
    self._split_args(line, 0, 0)
    self._command_processor.get_session().get_replication_policy(
        ).set_replication_allowed(False)
    self._print_info_if_verbose('Set replication policy to deny replication')