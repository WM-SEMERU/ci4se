def _init_objgoea(self, pop, assoc):
    propagate_counts = not self.args.no_propagate_counts
    return GOEnrichmentStudy(pop, assoc, self.godag, propagate_counts=
        propagate_counts, relationships=False, alpha=self.args.alpha,
        pvalcalc=self.args.pvalcalc, methods=self.methods)