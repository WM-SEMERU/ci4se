def describe_configs(self, config_resources, include_synonyms=False):
    version = self._matching_api_version(DescribeConfigsRequest)
    if version == 0:
        if include_synonyms:
            raise IncompatibleBrokerVersion(
                'include_synonyms requires DescribeConfigsRequest >= v1, which is not supported by Kafka {}.'
                .format(self.config['api_version']))
        request = DescribeConfigsRequest[version](resources=[self.
            _convert_describe_config_resource_request(config_resource) for
            config_resource in config_resources])
    elif version == 1:
        request = DescribeConfigsRequest[version](resources=[self.
            _convert_describe_config_resource_request(config_resource) for
            config_resource in config_resources], include_synonyms=
            include_synonyms)
    else:
        raise NotImplementedError(
            'Support for DescribeConfigs v{} has not yet been added to KafkaAdminClient.'
            .format(version))
    return self._send_request_to_node(self._client.least_loaded_node(), request
        )