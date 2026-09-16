def GetEstimatedYear(self):
    if self._preferred_year:
        return self._preferred_year
    if self._knowledge_base.year:
        return self._knowledge_base.year
    year = self._GetEarliestYearFromFileEntry()
    if not year:
        year = self._GetLatestYearFromFileEntry()
    if not year:
        year = timelib.GetCurrentYear()
    return year