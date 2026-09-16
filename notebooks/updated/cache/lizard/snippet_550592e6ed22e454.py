def make_fileitem_peinfo_resourceinfolist_resourceinfoitem_name(resource_name,
    condition='is', negate=False, preserve_case=False):
    document = 'FileItem'
    search = 'FileItem/PEInfo/ResourceInfoList/ResourceInfoItem/Name'
    content_type = 'string'
    content = resource_name
    ii_node = ioc_api.make_indicatoritem_node(condition, document, search,
        content_type, content, negate=negate, preserve_case=preserve_case)
    return ii_node