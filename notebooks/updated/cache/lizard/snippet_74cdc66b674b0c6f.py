def getEventFromUid(request, uid):
    events = []
    with suppress(ObjectDoesNotExist):
        events.append(SimpleEventPage.objects.get(uid=uid))
    with suppress(ObjectDoesNotExist):
        events.append(MultidayEventPage.objects.get(uid=uid))
    with suppress(ObjectDoesNotExist):
        events.append(RecurringEventPage.objects.get(uid=uid))
    if len(events) == 1:
        if events[0].isAuthorized(request):
            return events[0]
        else:
            return None
    elif len(events) == 0:
        raise ObjectDoesNotExist('No event with uid={}'.format(uid))
    else:
        raise MultipleObjectsReturned('Multiple events with uid={}'.format(uid)
            )