def GetPathFromLink(resource_link, resource_type=''):
    resource_link = TrimBeginningAndEndingSlashes(resource_link)
    if IsNameBased(resource_link):
        resource_link = urllib_quote(resource_link)
    if resource_type:
        return '/' + resource_link + '/' + resource_type + '/'
    else:
        return '/' + resource_link + '/'