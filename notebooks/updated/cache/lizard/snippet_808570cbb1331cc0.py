def get_observations(self):
    return [rpt for rpt in self._reports if rpt.report_type in self.OBS_TYPES]