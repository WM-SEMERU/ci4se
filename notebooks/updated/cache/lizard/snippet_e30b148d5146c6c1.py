def add_exception(self, exname, extype, exmsg):
    r
    if not isinstance(exname, str):
        raise RuntimeError('Argument `exname` is not valid')
    number = True
    try:
        int(exname)
    except ValueError:
        number = False
    if number:
        raise RuntimeError('Argument `exname` is not valid')
    if not isinstance(exmsg, str):
        raise RuntimeError('Argument `exmsg` is not valid')
    msg = ''
    try:
        raise extype(exmsg)
    except Exception as eobj:
        msg = _get_ex_msg(eobj)
    if msg != exmsg:
        raise RuntimeError('Argument `extype` is not valid')
    func_id, func_name = self._get_ex_data()
    if func_id not in self._ex_dict:
        self._ex_dict[func_id] = {}
    key = extype, exmsg
    exname = '{0}{1}{2}'.format(func_id, self._callables_separator, exname)
    entry = self._ex_dict[func_id].get(key, {'function': [], 'name': exname,
        'raised': []})
    if func_name not in entry['function']:
        entry['function'].append(func_name)
        entry['raised'].append(False)
    self._ex_dict[func_id][key] = entry
    return func_id, key, func_name