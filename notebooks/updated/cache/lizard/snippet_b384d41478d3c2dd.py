def do_removerep(self, line):
    mns = self._split_args(line, 1, -1)
    self._command_processor.get_session().get_replication_policy().repremove(
        mns)
    self._print_info_if_verbose('Removed {} from replication policy'.format
        (', '.join(mns)))