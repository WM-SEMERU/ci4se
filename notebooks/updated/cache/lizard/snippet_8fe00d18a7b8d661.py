def from_dict(cls, indicator):
    tags = indicator.get('tags')
    if tags is not None:
        tags = [Tag.from_dict(tag) for tag in tags]
    return Indicator(value=indicator.get('value'), type=indicator.get(
        'indicatorType'), priority_level=indicator.get('priorityLevel'),
        correlation_count=indicator.get('correlationCount'), whitelisted=
        indicator.get('whitelisted'), weight=indicator.get('weight'),
        reason=indicator.get('reason'), first_seen=indicator.get(
        'firstSeen'), last_seen=indicator.get('lastSeen'), sightings=
        indicator.get('sightings'), source=indicator.get('source'), notes=
        indicator.get('notes'), tags=tags, enclave_ids=indicator.get(
        'enclaveIds'))