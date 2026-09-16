def cl_picard(self, command, options, memscale=None):
    options = [('%s=%s' % (x, y)) for x, y in options]
    options.append('VALIDATION_STRINGENCY=SILENT')
    return self._get_picard_cmd(command, memscale=memscale) + options