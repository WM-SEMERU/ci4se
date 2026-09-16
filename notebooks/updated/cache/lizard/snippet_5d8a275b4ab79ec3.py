def _get_resource_access_state(self, request):
    feincms_page = self._get_page_from_path(request.path_info.lstrip('/'))
    if not feincms_page:
        return None
    INHERIT = AccessState.STATE_INHERIT
    while feincms_page.access_state == INHERIT and feincms_page.parent:
        feincms_page = feincms_page.parent
    never_restricted = INHERIT, AccessState.STATE_ALL_ALLOWED
    if feincms_page.access_state in never_restricted:
        return None
    return feincms_page.access_state