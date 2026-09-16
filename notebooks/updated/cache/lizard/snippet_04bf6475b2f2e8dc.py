def get_variable_days(self, year):
    days = super(LateSummer, self).get_variable_days(year)
    days.append((self.get_nth_weekday_in_month(year, 9, MON),
        'Late Summer Holiday'))
    return days