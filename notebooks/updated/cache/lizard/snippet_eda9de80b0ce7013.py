def _handle_value(self, value):
    if self._inspec:
        return value, ''
    if not self.list_values:
        mat = self._nolistvalue.match(value)
        if mat is None:
            raise SyntaxError()
        return mat.groups()
    mat = self._valueexp.match(value)
    if mat is None:
        raise SyntaxError()
    list_values, single, empty_list, comment = mat.groups()
    if list_values == '' and single is None:
        raise SyntaxError()
    if empty_list is not None:
        return [], comment
    if single is not None:
        if list_values and not single:
            single = None
        else:
            single = single or '""'
            single = self._unquote(single)
    if list_values == '':
        return single, comment
    the_list = self._listvalueexp.findall(list_values)
    the_list = [self._unquote(val) for val in the_list]
    if single is not None:
        the_list += [single]
    return the_list, comment