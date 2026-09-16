def format_span_json(span):
    span_json = {'displayName': utils.get_truncatable_str(span.name),
        'spanId': span.span_id, 'startTime': span.start_time, 'endTime':
        span.end_time, 'childSpanCount': len(span._child_spans)}
    parent_span_id = None
    if span.parent_span is not None:
        parent_span_id = span.parent_span.span_id
    if parent_span_id is not None:
        span_json['parentSpanId'] = parent_span_id
    if span.attributes:
        span_json['attributes'] = attributes.Attributes(span.attributes
            ).format_attributes_json()
    if span.stack_trace is not None:
        span_json['stackTrace'] = span.stack_trace.format_stack_trace_json()
    if span.time_events:
        span_json['timeEvents'] = {'timeEvent': [time_event.
            format_time_event_json() for time_event in span.time_events]}
    if span.links:
        span_json['links'] = {'link': [link.format_link_json() for link in
            span.links]}
    if span.status is not None:
        span_json['status'] = span.status.format_status_json()
    if span.same_process_as_parent_span is not None:
        span_json['sameProcessAsParentSpan'] = span.same_process_as_parent_span
    return span_json