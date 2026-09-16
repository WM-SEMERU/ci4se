def severity(self):
    resource_list = self.traffic_incident()
    severity = namedtuple('severity', 'severity')
    if len(resource_list) == 1 and resource_list[0] is None:
        return None
    else:
        try:
            return [severity(resource['severity']) for resource in
                resource_list]
        except (KeyError, TypeError):
            return [severity(resource['Severity']) for resource in
                resource_list]