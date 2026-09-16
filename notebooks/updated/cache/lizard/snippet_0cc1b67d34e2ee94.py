def stdin(self, line, prompt=True, timeout=3):
    if line == EOF:
        log('sending EOF...')
    else:
        log(_('sending input {}...').format(line))
    if prompt:
        try:
            self.process.expect('.+', timeout=timeout)
        except (TIMEOUT, EOF):
            raise Failure(_('expected prompt for input, found none'))
        except UnicodeDecodeError:
            raise Failure(_('output not valid ASCII text'))
    try:
        if line == EOF:
            self.process.sendeof()
        else:
            self.process.sendline(line)
    except OSError:
        pass
    return self