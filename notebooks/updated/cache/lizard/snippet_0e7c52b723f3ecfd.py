def admin_tools_render_menu(context, menu=None):
    if menu is None:
        menu = get_admin_menu(context)
    menu.init_with_context(context)
    has_bookmark_item = False
    bookmark = None
    if len([c for c in menu.children if isinstance(c, items.Bookmarks)]) > 0:
        has_bookmark_item = True
        url = context['request'].get_full_path()
        try:
            bookmark = Bookmark.objects.filter(user=context['request'].user,
                url=url)[0]
        except:
            pass
    context.update({'template': menu.template, 'menu': menu,
        'has_bookmark_item': has_bookmark_item, 'bookmark': bookmark,
        'admin_url': reverse('%s:index' % get_admin_site_name(context))})
    return context