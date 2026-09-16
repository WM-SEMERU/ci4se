def _initialize_metadata_service(cls):
    if cls.inited:
        return
    instance_id = cls.get_attribute('instance/id')
    if instance_id is not None:
        cls.is_running = True
        _GCP_METADATA_MAP['instance_id'] = instance_id
        for attribute_key, attribute_uri in _GCE_ATTRIBUTES.items():
            if attribute_key not in _GCP_METADATA_MAP:
                attribute_value = cls.get_attribute(attribute_uri)
                if attribute_value is not None:
                    _GCP_METADATA_MAP[attribute_key] = attribute_value
    cls.inited = True