def __getVariables(self):
    try:
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        output = subprocess.check_output(['p4', 'set'], startupinfo=startupinfo
            )
        if six.PY3:
            output = str(output, 'utf8')
    except subprocess.CalledProcessError as err:
        LOGGER.error(err)
        return
    p4vars = {}
    for line in output.splitlines():
        if not line:
            continue
        try:
            k, v = line.split('=', 1)
        except ValueError:
            continue
        p4vars[k.strip()] = v.strip().split(' (')[0]
        if p4vars[k.strip()].startswith('(config'):
            del p4vars[k.strip()]
    self._port = self._port or os.getenv('P4PORT', p4vars.get('P4PORT'))
    self._user = self._user or os.getenv('P4USER', p4vars.get('P4USER'))
    self._client = self._client or os.getenv('P4CLIENT', p4vars.get('P4CLIENT')
        )