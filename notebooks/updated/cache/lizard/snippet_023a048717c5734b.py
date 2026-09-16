def _replace_with_specific_page(page, menu_item):
    if type(page) is Page:
        page = page.specific
        if isinstance(menu_item, MenuItem):
            menu_item.link_page = page
        else:
            menu_item = page
    return page, menu_item