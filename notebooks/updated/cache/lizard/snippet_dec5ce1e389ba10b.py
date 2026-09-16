def folderitem(self, obj, item, index):
    title = obj.Title()
    description = obj.Description()
    url = obj.absolute_url()
    item['Description'] = description
    item['replace']['Title'] = get_link(url, value=title)
    retention_period = obj.getRetentionPeriod()
    if retention_period:
        hours = retention_period['hours']
        minutes = retention_period['minutes']
        days = retention_period['days']
        item['RetentionPeriod'] = _('hours: {} minutes: {} days: {}'.format
            (hours, minutes, days))
    else:
        item['RetentionPeriod'] = ''
    sample_matrix = obj.getSampleMatrix()
    if sample_matrix:
        title = sample_matrix.Title()
        url = sample_matrix.absolute_url()
        item['SampleMatrix'] = title
        item['replace']['SampleMatrix'] = get_link(url, value=title)
    else:
        item['SampleMatrix'] = ''
    container_type = obj.getContainerType()
    if container_type:
        title = container_type.Title()
        url = container_type.absolute_url()
        item['ContainerType'] = title
        item['replace']['ContainerType'] = get_link(url, value=title)
    else:
        item['ContainerType'] = ''
    sample_points = obj.getSamplePoints()
    if sample_points:
        links = map(lambda sp: get_link(sp.absolute_url(), value=sp.Title(),
            css_class='link'), sample_points)
        item['replace']['getSamplePoints'] = ', '.join(links)
    else:
        item['getSamplePoints'] = ''
    return item