def select_files(self, what='o'):
    choices = collections.OrderedDict([('i', self.input_file), ('o', self.
        output_file), ('f', self.files_file), ('j', self.job_file), ('l',
        self.log_file), ('e', self.stderr_file), ('q', self.qout_file)])
    if what == 'all':
        return [getattr(v, 'path') for v in choices.values()]
    selected = []
    for c in what:
        try:
            selected.append(getattr(choices[c], 'path'))
        except KeyError:
            logger.warning('Wrong keyword %s' % c)
    return selected