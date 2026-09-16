def visitIriRange(self, ctx: ShExDocParser.IriRangeContext):
    baseiri = self.context.iri_to_iriref(ctx.iri())
    if not ctx.STEM_MARK():
        vsvalue = baseiri
    elif ctx.iriExclusion():
        vsvalue = IriStemRange(baseiri, exclusions=[])
        self._iri_exclusions(vsvalue, ctx.iriExclusion())
    else:
        vsvalue = IriStem(baseiri)
    self.nodeconstraint.values.append(vsvalue)