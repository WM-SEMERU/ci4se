def _get_content(context, page, content_type, lang, fallback=True):
    if not page:
        return ''
    if not lang and 'lang' in context:
        lang = context.get('lang', pages_settings.PAGE_DEFAULT_LANGUAGE)
    page = get_page_from_string_or_id(page, lang)
    if not page:
        return ''
    content = Content.objects.get_content(page, lang, content_type, fallback)
    return content