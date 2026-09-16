def gt_bases(self):
    result = []
    for a in self.gt_alleles:
        if a is None:
            result.append(None)
        elif a == 0:
            result.append(self.site.REF)
        else:
            result.append(self.site.ALT[a - 1].value)
    return tuple(result)