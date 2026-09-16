def request(self, confirmed=False, timeout=None, persist=None):
    node = new_ele('commit')
    if confirmed:
        self._assert(':confirmed-commit')
        sub_ele(node, 'confirmed')
        if timeout is not None:
            sub_ele(node, 'confirm-timeout').text = timeout
        if persist is not None:
            sub_ele(node, 'persist').text = persist
    return self._request(node)