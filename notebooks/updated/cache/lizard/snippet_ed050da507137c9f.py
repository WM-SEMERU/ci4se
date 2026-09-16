def _getEventFromUid(self, request, uid):
    event = getEventFromUid(request, uid)
    home = request.site.root_page
    if event.get_ancestors().filter(id=home.id).exists():
        return event