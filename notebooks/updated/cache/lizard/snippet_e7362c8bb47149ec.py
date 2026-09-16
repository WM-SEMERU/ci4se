def endpoint_loader(request, application, model, **kwargs):
    if request.method != 'POST':
        raise AJAXError(400, _('Invalid HTTP method used.'))
    try:
        module = import_module('%s.endpoints' % application)
    except ImportError as e:
        if settings.DEBUG:
            raise e
        else:
            raise AJAXError(404, _('AJAX endpoint does not exist.'))
    if hasattr(module, model):
        endpoint = getattr(module, model)
    else:
        method = kwargs.get('method', 'create').lower()
        try:
            del kwargs['method']
        except:
            pass
        try:
            model_endpoint = ajax.endpoint.load(model, application, method,
                **kwargs)
            if not model_endpoint.authenticate(request, application, method):
                raise AJAXError(403, _('User is not authorized.'))
            endpoint = getattr(model_endpoint, method, False)
            if not endpoint:
                raise AJAXError(404, _('Invalid method.'))
        except NotRegistered:
            raise AJAXError(500, _('Invalid model.'))
    data = endpoint(request)
    if isinstance(data, HttpResponse):
        return data
    if isinstance(data, EnvelopedResponse):
        envelope = data.metadata
        payload = data.data
    else:
        envelope = {}
        payload = data
    envelope.update({'success': True, 'data': payload})
    return HttpResponse(json.dumps(envelope, cls=DjangoJSONEncoder,
        separators=(',', ':')))