def level_i18n_name(self):
    for level, name in spatial_granularities:
        if self.level == level:
            return name
    return self.level_name