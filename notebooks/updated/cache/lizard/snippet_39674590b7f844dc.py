def get_specification_info(self, obj):
    info = self.get_base_info(obj)
    results_range = obj.getResultsRange()
    info.update({'results_range': results_range, 'sample_type_uid': obj.
        getSampleTypeUID(), 'sample_type_title': obj.getSampleTypeTitle(),
        'client_uid': obj.getClientUID()})
    bsc = api.get_tool('bika_setup_catalog')

    def get_service_by_keyword(keyword):
        if keyword is None:
            return []
        return map(api.get_object, bsc({'portal_type': 'AnalysisService',
            'getKeyword': keyword}))
    specifications = {}
    for spec in results_range:
        service_uid = spec.get('uid')
        if service_uid is None:
            for service in get_service_by_keyword(spec.get('keyword')):
                service_uid = api.get_uid(service)
                specifications[service_uid] = spec
            continue
        specifications[service_uid] = spec
    info['specifications'] = specifications
    info['service_uids'] = specifications.keys()
    return info