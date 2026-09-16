def addError(self, test, err, capt=None):
    exc_type, exc_val, tb = err
    tb = ''.join(traceback.format_exception(exc_type, exc_val if isinstance
        (exc_val, exc_type) else exc_type(exc_val), tb))
    name = id_split(test.id())
    group = self.report_data[name[0]]
    if issubclass(err[0], SkipTest):
        type = 'skipped'
        self.stats['skipped'] += 1
        group.stats['skipped'] += 1
    else:
        type = 'error'
        self.stats['errors'] += 1
        group.stats['errors'] += 1
    group.tests.append({'name': name[-1], 'failed': True, 'type': type,
        'errtype': nice_classname(err[0]), 'message': exc_message(err),
        'tb': tb})