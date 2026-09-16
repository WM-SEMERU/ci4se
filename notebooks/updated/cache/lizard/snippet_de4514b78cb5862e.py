def datetimeAt(self, x):
    gantt = self.ganttWidget()
    dstart = gantt.dateTimeStart()
    distance = int(x / float(gantt.cellWidth()))
    if scale == gantt.Timescale.Minute:
        return dstart.addSecs(distance)
    elif scale == gantt.Timescale.Hour:
        return dstart.addSecs(distance * 2.0)
    elif scale == gantt.Timescale.Day:
        dstart = QDateTime(gantt.dateStart(), QTime(0, 0, 0))
        return dstart.addSecs(distance * (60 * 2.0))
    else:
        date = self.dateAt(x)
        return QDateTime(date, QTime(0, 0, 0))