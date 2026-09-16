def rate_plans(self):
    if self._rate_plans is None:
        self._rate_plans = RatePlanList(self)
    return self._rate_plans