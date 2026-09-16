def process_event(self, event_id):
    with db.session.begin_nested():
        event = Event.query.get(event_id)
        event._celery_task = self
        event.receiver.run(event)
        flag_modified(event, 'response')
        flag_modified(event, 'response_headers')
        db.session.add(event)
    db.session.commit()