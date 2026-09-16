def dataoneTypes(request):
    if is_v1_api(request):
        return d1_common.types.dataoneTypes_v1_1
    elif is_v2_api(request) or is_diag_api(request):
        return d1_common.types.dataoneTypes_v2_0
    else:
        raise d1_common.types.exceptions.ServiceFailure(0,
            'Unknown version designator in URL. url="{}"'.format(request.path))