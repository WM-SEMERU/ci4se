def _check(self, accepted):
    total = []
    if 1 in self.quickresponse:
        total = total + self.quickresponse[1]
    if (1, 0) in self.quickresponse:
        total = total + self.quickresponse[1, 0]
    for key in total:
        if (key.id == 1 or key.id == (1, 0)) and key.type == 3:
            if accepted is None:
                if 2 in key.trans:
                    return key.trans[2]
            else:
                for state in accepted:
                    if (2, state) in key.trans:
                        return key.trans[2, state]
    return -1