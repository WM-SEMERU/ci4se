def roll_edits_hdfs(self, nameservice=None):
    args = dict()
    if nameservice:
        args['nameservice'] = nameservice
    return self._cmd('hdfsRollEdits', data=args)