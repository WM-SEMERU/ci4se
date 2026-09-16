def pages_siblings_menu(context, page, url='/'):
    lang = context.get('lang', pages_settings.PAGE_DEFAULT_LANGUAGE)
    page = get_page_from_string_or_id(page, lang)
    if page:
        if page.parent:
            root = page.parent
        else:
            root = page
        children = root.get_children_for_frontend()
        context.update({'children': children, 'page': page})
    return context