def display(self):
    if self.degree and self.school:
        disp = self.degree + ' from ' + self.school
    else:
        disp = self.degree or self.school or None
    if disp is not None and self.date_range is not None:
        disp += ' (%d-%d)' % self.date_range.years_range
    return disp or ''