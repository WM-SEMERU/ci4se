def run(self):
    self._logger.info('running for <{url}>'.format(url=self._url))
    args = format_args(self._options)
    self._logger.debug('command: `{cmd}` / args: {args}'.format(cmd=self.
        _cmd, args=args))
    try:
        process = Popen(args=[self._cmd] + args, stdin=PIPE, stdout=PIPE,
            stderr=PIPE)
        pid = process.pid
        self._logger.debug('running as PID #{pid}'.format(pid=pid))
    except OSError as ex:
        raise PhantomasRunError('Failed to run phantomas: {0}'.format(ex),
            ex.errno)
    try:
        stdout, stderr = process.communicate()
        returncode = process.returncode
    except Exception:
        raise PhantomasRunError('Failed to complete the run')
    stdout = stdout.decode('utf8')
    stderr = stderr.decode('utf8')
    self._logger.debug('completed with return code #{returncode}'.format(
        returncode=returncode))
    if stderr != '':
        self._logger.debug('stderr: {stderr}'.format(stderr=stderr))
        raise PhantomasFailedError(stderr.strip(), returncode)
    try:
        results = json.loads(stdout)
    except Exception:
        raise PhantomasResponseParsingError('Unable to parse the response')
    if self._options.get('runs', 0) > 1:
        return Runs(self._url, results)
    else:
        return Results(self._url, results)