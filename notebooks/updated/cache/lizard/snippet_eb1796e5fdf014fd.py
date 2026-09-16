def parse_requested_expands(query_key, request):
    requested_expands = []
    for key, val in request.params.items():
        if key == query_key:
            requested_expands += val.split(',')
    return requested_expands