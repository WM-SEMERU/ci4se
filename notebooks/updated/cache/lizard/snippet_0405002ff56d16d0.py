def _helper_wrefs(self, targets, recurse=True):
    for c in self:
        if isinstance(c, Word) or isinstance(c, Morpheme) or isinstance(c,
            Phoneme):
            targets.append(c)
        elif isinstance(c, WordReference):
            try:
                targets.append(self.doc[c.id])
            except KeyError:
                targets.append(c)
        elif isinstance(c, AbstractSpanAnnotation) and recurse:
            c._helper_wrefs(targets)
        elif isinstance(c, Correction) and c.auth:
            for e in c:
                if isinstance(e, AbstractCorrectionChild) and e.auth:
                    for e2 in e:
                        if isinstance(e2, AbstractSpanAnnotation):
                            e2._helper_wrefs(targets)