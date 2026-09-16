def change_aliases(self, commands):
    body = {'actions': [{command: dict(index=index, alias=alias, **params)} for
        command, index, alias, params in commands]}
    return self.conn._send_request('POST', '_aliases', body)