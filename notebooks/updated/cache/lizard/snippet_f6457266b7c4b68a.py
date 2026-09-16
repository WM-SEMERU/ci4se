def season(self):
    try:
        self._season
    except AttributeError:
        self._season = self._mission.Season(self.ID)
        if hasattr(self._season, '__len__'):
            raise AttributeError(
                'Please choose a campaign/season for this target: %s.' %
                self._season)
    return self._season