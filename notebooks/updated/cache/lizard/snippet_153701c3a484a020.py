def addMeal(self, date, category, name, notes=None, prices=None, roles=None):
    if self.legendData:
        name, notes = extractNotes(name, notes or [], legend=self.
            legendData, key=self.legendKeyFunc, regex=self.extra_regex)
    prices = buildPrices(prices or {}, roles, default=self.
        additionalCharges[0], additional=self.additionalCharges[1])
    if len(name) > 250:
        name = name[:247] + '...'
    super(LazyBuilder, self).addMeal(extractDate(date), category, name, 
        notes or [], prices)