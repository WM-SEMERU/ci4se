def distinct_value_fractions(self):
    return pd.DataFrame([(c.dcount() / float(self.size())) for c in self.
        columns()], index=[c.name() for c in self.columns()], columns=[
        'fraction'])