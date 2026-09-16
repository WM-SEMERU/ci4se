def create_events(self, kwargs_list):
    uuid_map = {kwargs.get('uuid', ''): {'actors': kwargs.pop('actors', []),
        'ignore_duplicates': kwargs.pop('ignore_duplicates', False),
        'event_kwargs': kwargs} for kwargs in kwargs_list}
    uuid_set = set(Event.objects.filter(uuid__in=uuid_map.keys()).
        values_list('uuid', flat=True))
    for uuid, event_dict in uuid_map.items():
        event_dict['exists'] = uuid in uuid_set
    events_to_create = []
    for uuid, event_dict in uuid_map.items():
        if not event_dict['exists'] or not event_dict['ignore_duplicates']:
            events_to_create.append(Event(**event_dict['event_kwargs']))
    created_events = Event.objects.bulk_create(events_to_create)
    event_actors_to_create = []
    for created_event in created_events:
        event_dict = uuid_map[created_event.uuid]
        if event_dict['actors'] is not None:
            for actor in event_dict['actors']:
                actor_id = actor.id if hasattr(actor, 'id') else actor
                event_actors_to_create.append(EventActor(entity_id=actor_id,
                    event=created_event))
    EventActor.objects.bulk_create(event_actors_to_create)
    return created_events