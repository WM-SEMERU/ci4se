def _impopts(self, opts):
    optstr = ''
    if len(opts):
        for key in opts:
            if len(str(opts[key])):
                if key == 'datarow':
                    optstr += 'datarow=' + str(opts[key]) + ';'
                elif key == 'delimiter':
                    optstr += 'delimiter='
                    optstr += "'" + '%02x' % ord(opts[key].encode(self._io.
                        sascfg.encoding)) + "'x; "
                elif key == 'getnames':
                    optstr += 'getnames='
                    if opts[key]:
                        optstr += 'YES; '
                    else:
                        optstr += 'NO; '
                elif key == 'guessingrows':
                    optstr += 'guessingrows='
                    if opts[key] == 'MAX':
                        optstr += 'MAX; '
                    else:
                        optstr += str(opts[key]) + '; '
    return optstr