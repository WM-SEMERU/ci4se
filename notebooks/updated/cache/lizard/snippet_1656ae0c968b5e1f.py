def remove_service(self, service):
    uid = api.get_uid(service)
    services = self.getAnalyses()
    num_services = len(services)
    services = [item for item in services if item.get('service_uid', '') != uid
        ]
    removed = len(services) < num_services
    self.setAnalyses(services)
    settings = self.getAnalysisServicesSettings()
    settings = [item for item in settings if item.get('uid', '') != uid]
    self.setAnalysisServicesSettings(settings)
    return removed