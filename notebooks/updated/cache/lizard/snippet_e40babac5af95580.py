def show_abierrors(self, nids=None, stream=sys.stdout):
    lines = []
    app = lines.append
    for task in self.iflat_tasks(status=self.S_ABICRITICAL, nids=nids):
        header = '=== ' + task.qout_file.path + '==='
        app(header)
        report = task.get_event_report()
        if report is not None:
            app('num_errors: %s, num_warnings: %s, num_comments: %s' % (
                report.num_errors, report.num_warnings, report.num_comments))
            app('*** ERRORS ***')
            app('\n'.join(str(e) for e in report.errors))
            app('*** BUGS ***')
            app('\n'.join(str(b) for b in report.bugs))
        else:
            app('get_envent_report returned None!')
        app('=' * len(header) + 2 * '\n')
    return stream.writelines(lines)