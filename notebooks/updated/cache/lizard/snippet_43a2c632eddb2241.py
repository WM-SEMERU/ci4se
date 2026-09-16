def show_revisions(context, page, content_type, lang=None):
    if not pages_settings.PAGE_CONTENT_REVISION:
        return {'revisions': None}
    revisions = Content.objects.filter(page=page, language=lang, type=
        content_type).order_by('-creation_date')
    if len(revisions) < 2:
        return {'revisions': None}
    return {'revisions': revisions[0:10]}