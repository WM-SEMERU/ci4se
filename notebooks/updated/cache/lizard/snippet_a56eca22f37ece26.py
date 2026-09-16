def api_headers_tween_factory(handler, registry):

    def api_headers_tween(request):
        response = handler(request)
        set_version(request, response)
        set_req_guid(request, response)
        return response
    return api_headers_tween