def dump_to_response(request, app_label=None, exclude=None, filename_prefix
    =None):
    app_label = app_label or []
    exclude = exclude
    try:
        filename = '%s.%s' % (datetime.now().isoformat(), settings.
            SMUGGLER_FORMAT)
        if filename_prefix:
            filename = '%s_%s' % (filename_prefix, filename)
        if not isinstance(app_label, list):
            app_label = [app_label]
        response = serialize_to_response(app_label, exclude)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    except CommandError as e:
        messages.error(request, _(
            'An exception occurred while dumping data: %s') % force_text(e))
    return HttpResponseRedirect(request.build_absolute_uri().split('dump')[0])