def dateXPos(self, date):
    gantt = self.ganttWidget()
    distance = gantt.dateStart().daysTo(date)
    return gantt.cellWidth() * distance