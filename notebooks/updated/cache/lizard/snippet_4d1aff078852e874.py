def count(self, strand, pseudo=False):
    if pseudo:
        cmd_args = ['-pseudo']
    else:
        cmd_args = []
    stdout = self._run('count', cmd_args, [str(strand)]).split('\n')
    return int(float(stdout[-2]))