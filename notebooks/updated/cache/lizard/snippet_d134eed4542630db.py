def filterVariantAnnotation(self, vann):
    ret = False
    if len(self._effects) != 0 and not vann.transcript_effects:
        return False
    elif len(self._effects) == 0:
        return True
    for teff in vann.transcript_effects:
        if self.filterEffect(teff):
            ret = True
    return ret