def _execCmd(self, cmd, args):
    output = self._eslconn.api(cmd, args)
    if output:
        body = output.getBody()
        if body:
            return body.splitlines()
    return None