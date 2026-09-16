def eval(self, command):
    for cmd, response in self.response_list:
        if not cmd.match(command):
            continue
        if response is None:
            return None
        elif hasattr(response, '__call__'):
            return response(command)
        else:
            return response
    if self.strict:
        raise Exception('Undefined command: ' + repr(command))
    return None