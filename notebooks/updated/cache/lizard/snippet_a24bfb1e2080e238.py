def aws_xray_trace_config(name=None):

    def _trace_config_ctx_factory(trace_request_ctx):
        return SimpleNamespace(name=name, trace_request_ctx=trace_request_ctx)
    trace_config = aiohttp.TraceConfig(trace_config_ctx_factory=
        _trace_config_ctx_factory)
    trace_config.on_request_start.append(begin_subsegment)
    trace_config.on_request_end.append(end_subsegment)
    trace_config.on_request_exception.append(end_subsegment_with_exception)
    return trace_config