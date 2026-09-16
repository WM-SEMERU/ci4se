def folderitem(self, obj, item, index):
    url = obj.absolute_url()
    title = obj.Title()
    item['Description'] = obj.Description()
    item['replace']['Title'] = get_link(url, value=title)
    after_icons = ''
    if obj.getBlank():
        after_icons += get_image('blank.png', title=t(_('Blank')))
    if obj.getHazardous():
        after_icons += get_image('hazardous.png', title=t(_('Hazardous')))
    if after_icons:
        item['after']['Title'] = after_icons
    return item