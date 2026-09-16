def open_shell(self, i_stream='stdin', o_stream='stdout stderr',
    working_directory=None, env_vars=None, noprofile=False, codepage=437,
    lifetime=None, idle_timeout=None):
    req = {'env:Envelope': self._get_soap_header(resource_uri=
        'http://schemas.microsoft.com/wbem/wsman/1/windows/shell/cmd',
        action='http://schemas.xmlsoap.org/ws/2004/09/transfer/Create')}
    header = req['env:Envelope']['env:Header']
    header['w:OptionSet'] = {'w:Option': [{'@Name': 'WINRS_NOPROFILE',
        '#text': str(noprofile).upper()}, {'@Name': 'WINRS_CODEPAGE',
        '#text': str(codepage)}]}
    shell = req['env:Envelope'].setdefault('env:Body', {}).setdefault(
        'rsp:Shell', {})
    shell['rsp:InputStreams'] = i_stream
    shell['rsp:OutputStreams'] = o_stream
    if working_directory:
        shell['rsp:WorkingDirectory'] = working_directory
    if idle_timeout:
        shell['rsp:IdleTimeOut'] = idle_timeout
    if env_vars:
        env = shell.setdefault('rsp:Environment', {})
        for key, value in env_vars.items():
            env['rsp:Variable'] = {'@Name': key, '#text': value}
    res = self.send_message(xmltodict.unparse(req))
    root = ET.fromstring(res)
    return next(node for node in root.findall('.//*') if node.get('Name') ==
        'ShellId').text