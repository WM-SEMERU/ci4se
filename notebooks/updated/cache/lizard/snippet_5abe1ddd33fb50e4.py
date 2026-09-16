def process_raw_data(cls, raw_data):
    properties = raw_data.get('properties', {})
    raw_metadata = raw_data.get('resourceMetadata', None)
    if raw_metadata is not None:
        metadata = ResourceMetadata.from_raw_data(raw_metadata)
        raw_data['resourceMetadata'] = metadata
    raw_state = properties.get('configurationState', None)
    if raw_state is not None:
        configuration = ConfigurationState.from_raw_data(raw_state)
        properties['configurationState'] = configuration
    return super(_BaseHNVModel, cls).process_raw_data(raw_data)