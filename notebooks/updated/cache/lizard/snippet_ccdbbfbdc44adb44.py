def solve(self):
    popflag = True
    self.tmpopslist = []
    while True:
        while self.opslist and popflag:
            op = self.opslist.pop()
            if self.is_variable(op):
                op = self.variables.get(op)
            if self.is_operator(op):
                popflag = False
                break
            self.tmpopslist.append(op)
        tmpr = self._get_temp_result(op)
        if tmpr == 'ERROR':
            return None
        if tmpr is not None:
            self.opslist.append('{r:.20f}'.format(r=tmpr))
        if len(self.tmpopslist) > 0 or len(self.opslist) > 1:
            popflag = True
        else:
            break
    return float(self.opslist[0])