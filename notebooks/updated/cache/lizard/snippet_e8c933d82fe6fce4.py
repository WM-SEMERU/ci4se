def _getEventsByDay(self, request, firstDay, lastDay):
    return getAllEventsByDay(request, firstDay, lastDay, home=self)