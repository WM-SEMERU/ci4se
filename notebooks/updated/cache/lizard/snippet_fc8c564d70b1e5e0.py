def make_fileitem_peinfo_petimestamp(compile_time, condition='is', negate=False
    ):
    document = 'FileItem'
    search = 'FileItem/PEInfo/PETimeStamp'
    content_type = 'date'
    content = compile_time
    ii_node = ioc_api.make_indicatoritem_node(condition, document, search,
        content_type, content, negate=negate)
    return ii_node