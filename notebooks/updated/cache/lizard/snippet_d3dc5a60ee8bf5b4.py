def _check_result(self):
    if not self.__call_result:
        raise CommandExecutionError('No output result from Zypper?')
    self.exit_code = self.__call_result['retcode']
    if self._is_lock():
        return False
    if self._is_error():
        _error_msg = list()
        if not self._is_xml_mode():
            msg = self.__call_result['stderr'] and self.__call_result['stderr'
                ].strip() or ''
            if msg:
                _error_msg.append(msg)
        else:
            try:
                doc = dom.parseString(self.__call_result['stdout'])
            except ExpatError as err:
                log.error(err)
                doc = None
            if doc:
                msg_nodes = doc.getElementsByTagName('message')
                for node in msg_nodes:
                    if node.getAttribute('type') == 'error':
                        _error_msg.append(node.childNodes[0].nodeValue)
            elif self.__call_result['stderr'].strip():
                _error_msg.append(self.__call_result['stderr'].strip())
        self.error_msg = _error_msg
    return True