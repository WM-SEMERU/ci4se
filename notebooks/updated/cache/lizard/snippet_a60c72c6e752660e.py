def request(self, confirmed=False, timeout=None, comment=None, synchronize=
    False, at_time=None, check=False):
    node = new_ele_ns('commit-configuration', '')
    if confirmed and at_time is not None:
        raise NCClientError(
            "'Commit confirmed' and 'commit at' are mutually exclusive.")
    if confirmed:
        self._assert(':confirmed-commit')
        sub_ele(node, 'confirmed')
        if timeout is not None:
            timeout_int = int(timeout) if isinstance(timeout, str) else timeout
            sub_ele(node, 'confirm-timeout').text = str(int(math.ceil(
                timeout_int / 60.0)))
    elif at_time is not None:
        sub_ele(node, 'at-time').text = at_time
    if comment is not None:
        sub_ele(node, 'log').text = comment
    if synchronize:
        sub_ele(node, 'synchronize')
    if check:
        sub_ele(node, 'check')
    return self._request(node)