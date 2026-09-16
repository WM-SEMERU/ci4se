def top_referrers(self, domain_only=True):
    referrer = self._referrer_clause(domain_only)
    return self.get_query().select(referrer, fn.Count(PageView.id)).group_by(
        referrer).order_by(fn.Count(PageView.id).desc()).tuples()