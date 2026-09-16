def create(self, friendly_name, inbound_request_url=values.unset,
    inbound_method=values.unset, fallback_url=values.unset, fallback_method
    =values.unset, status_callback=values.unset, sticky_sender=values.unset,
    mms_converter=values.unset, smart_encoding=values.unset,
    scan_message_content=values.unset, fallback_to_long_code=values.unset,
    area_code_geomatch=values.unset, validity_period=values.unset,
    synchronous_validation=values.unset):
    data = values.of({'FriendlyName': friendly_name, 'InboundRequestUrl':
        inbound_request_url, 'InboundMethod': inbound_method, 'FallbackUrl':
        fallback_url, 'FallbackMethod': fallback_method, 'StatusCallback':
        status_callback, 'StickySender': sticky_sender, 'MmsConverter':
        mms_converter, 'SmartEncoding': smart_encoding,
        'ScanMessageContent': scan_message_content, 'FallbackToLongCode':
        fallback_to_long_code, 'AreaCodeGeomatch': area_code_geomatch,
        'ValidityPeriod': validity_period, 'SynchronousValidation':
        synchronous_validation})
    payload = self._version.create('POST', self._uri, data=data)
    return ServiceInstance(self._version, payload)