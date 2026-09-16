def make_serviceitem_servicedllsignatureverified(dll_sig_verified,
    condition='is', negate=False):
    document = 'ServiceItem'
    search = 'ServiceItem/serviceDLLSignatureVerified'
    content_type = 'bool'
    content = dll_sig_verified
    ii_node = ioc_api.make_indicatoritem_node(condition, document, search,
        content_type, content, negate=negate)
    return ii_node