def export(self, top=True):
    out = []
    if top:
        out.append(self._internal_name)
    out.append(self._to_str(self.typical_or_extreme_period_name))
    out.append(self._to_str(self.typical_or_extreme_period_type))
    out.append(self._to_str(self.period_start_day))
    out.append(self._to_str(self.period_end_day))
    return ','.join(out)