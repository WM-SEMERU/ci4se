def convert_2_utc(self, datetime_, timezone):
    datetime_ = self.tz_mapper[timezone].localize(datetime_)
    return datetime_.astimezone(pytz.UTC)