def _run_link(self, stream=sys.stdout, dry_run=False, stage_files=True,
    resubmit_failed=False):
    if resubmit_failed:
        self.args['action'] = 'resubmit'
    argv = self._make_argv()
    if dry_run:
        argv.append('--dry_run')
    self._invoke(argv, stream, resubmit_failed=resubmit_failed)