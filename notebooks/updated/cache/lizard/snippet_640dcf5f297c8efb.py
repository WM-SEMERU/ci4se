def update_qos_aggregated_configuration(self, qos_configuration, timeout=-1):
    uri = '{}{}'.format(self.data['uri'], self.QOS_AGGREGATED_CONFIGURATION)
    return self._helper.update(qos_configuration, uri=uri, timeout=timeout)