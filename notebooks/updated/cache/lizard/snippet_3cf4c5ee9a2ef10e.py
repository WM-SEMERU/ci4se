def serialize(self):
    return {'syear': self.syear, 'smon': self.smon, 'smday': self.smday,
        'swday': self.swday, 'swday_offset': self.swday_offset, 'eyear':
        self.eyear, 'emon': self.emon, 'emday': self.emday, 'ewday': self.
        ewday, 'ewday_offset': self.ewday_offset, 'skip_interval': self.
        skip_interval, 'other': self.other, 'timeranges': [t.serialize() for
        t in self.timeranges]}