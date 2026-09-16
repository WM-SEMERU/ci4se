def dist_string(self, val_meters):
    if self.settings.dist_unit == 'nm':
        return '%.1fnm' % (val_meters * 0.000539957)
    if self.settings.dist_unit == 'miles':
        return '%.1fmiles' % (val_meters * 0.000621371)
    return '%um' % val_meters