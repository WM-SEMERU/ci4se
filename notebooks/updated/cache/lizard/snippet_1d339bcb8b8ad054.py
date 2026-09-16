def before_http_request(request, current_span_extractor):
    span = utils.start_child_span(operation_name=request.operation, parent=
        current_span_extractor())
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    span.set_tag(tags.HTTP_URL, request.full_url)
    service_name = request.service_name
    host, port = request.host_port
    if service_name:
        span.set_tag(tags.PEER_SERVICE, service_name)
    if host:
        span.set_tag(tags.PEER_HOST_IPV4, host)
    if port:
        span.set_tag(tags.PEER_PORT, port)
    for interceptor in ClientInterceptors.get_interceptors():
        interceptor.process(request=request, span=span)
    try:
        carrier = {}
        opentracing.tracer.inject(span_context=span.context, format=Format.
            HTTP_HEADERS, carrier=carrier)
        for key, value in six.iteritems(carrier):
            request.add_header(key, value)
    except opentracing.UnsupportedFormatException:
        pass
    return span