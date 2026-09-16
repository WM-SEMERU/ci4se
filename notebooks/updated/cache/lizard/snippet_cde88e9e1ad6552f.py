def webhooks_v2(request):
    if request.method != 'POST':
        return HttpResponse('Invalid Request.', status=400)
    try:
        event_json = simplejson.loads(request.body)
    except AttributeError:
        event_json = simplejson.loads(request.raw_post_data)
    event_key = event_json['type'].replace('.', '_')
    if event_key in WEBHOOK_MAP:
        WEBHOOK_MAP[event_key].send(sender=None, full_json=event_json)
    return HttpResponse(status=200)