def server_group_list(request):
    try:
        return api.nova.server_group_list(request)
    except Exception:
        exceptions.handle(request, _('Unable to retrieve Nova server groups.'))
        return []