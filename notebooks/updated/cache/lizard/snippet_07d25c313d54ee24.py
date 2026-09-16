def SetTimelineOwner(self, username):
    self._timeline_owner = username
    logger.info('Owner of the timeline: {0!s}'.format(self._timeline_owner))