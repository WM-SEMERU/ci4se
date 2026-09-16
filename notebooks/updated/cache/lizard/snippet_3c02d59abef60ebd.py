def getMe(self):
    response_str = self._command('getMe')
    if not response_str:
        return False
    response = json.loads(response_str)
    return response