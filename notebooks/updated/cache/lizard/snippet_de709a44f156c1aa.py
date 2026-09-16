def delete_event(self, calendar_id, event_id):
    self.request_handler.delete(endpoint='calendars/%s/events' %
        calendar_id, data={'event_id': event_id})