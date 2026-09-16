def render_title_tag(context, is_og=False):
    request = context['request']
    content = ''
    if context.get('object'):
        try:
            content = context['object'].get_meta_title()
        except AttributeError:
            pass
    elif context.get('meta_tagger'):
        content = context['meta_tagger'].get('title')
    if not content:
        try:
            content = request.current_page.get_page_title()
            if not content:
                content = request.current_page.get_title()
        except (AttributeError, NoReverseMatch):
            pass
    if not is_og:
        return content
    else:
        return mark_safe('<meta property="og:title" content="{content}">'.
            format(content=content))