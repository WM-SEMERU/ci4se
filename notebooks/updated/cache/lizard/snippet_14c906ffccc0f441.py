def _upcoming_datetime_from(self):
    nextDt = self.__localAfter(timezone.localtime(), dt.time.max,
        excludeCancellations=True, excludeExtraInfo=True)
    return nextDt