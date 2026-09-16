def _refresh_context(self):
    header_str = os.getenv(LAMBDA_TRACE_HEADER_KEY)
    trace_header = TraceHeader.from_header_str(header_str)
    if not global_sdk_config.sdk_enabled():
        trace_header._sampled = False
    segment = getattr(self._local, 'segment', None)
    if segment:
        if not trace_header.root or trace_header.root == segment.trace_id:
            return
        else:
            self._initialize_context(trace_header)
    else:
        self._initialize_context(trace_header)