def dateTimeRect(self, dateTime):
    data = self._dateTimeGrid.get(dateTime.toTime_t())
    if data:
        return QRectF(data[1])
    return QRectF()