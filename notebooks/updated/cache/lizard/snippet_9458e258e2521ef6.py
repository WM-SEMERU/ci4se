def fix_related_item_tag(dom):
    location = dom.match('mods:mods', 'mods:relatedItem', 'mods:location')
    if not location:
        return
    location = first(location)
    location.replaceWith(dhtmlparser.HTMLElement())
    related_item = dom.match('mods:mods', 'mods:relatedItem')
    related_item = first(related_item)
    if not related_item.getContent().strip():
        related_item.replaceWith(dhtmlparser.HTMLElement())