def zapier_guest_hook(request):
    if request.META.get('HTTP_X_ZAPIER_SECRET', None
        ) != settings.WAFER_TICKETS_SECRET:
        raise PermissionDenied('Incorrect secret')
    payload = json.loads(request.body.decode('utf8'))
    import_ticket(payload['barcode'], payload['ticket_type'], payload['email'])
    return HttpResponse('Noted\n', content_type='text/plain')