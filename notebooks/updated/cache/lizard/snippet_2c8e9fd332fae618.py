def _extract_annotations_from_span(span):
    if span.time_events is None:
        return []
    annotations = []
    for time_event in span.time_events:
        annotation = time_event.annotation
        if not annotation:
            continue
        event_timestamp_mus = timestamp_to_microseconds(time_event.timestamp)
        annotations.append({'timestamp': int(round(event_timestamp_mus)),
            'value': annotation.description})
    return annotations