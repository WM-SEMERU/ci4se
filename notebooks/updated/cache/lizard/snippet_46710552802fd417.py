def _construct_rest_api(self):
    rest_api = ApiGatewayRestApi(self.logical_id, depends_on=self.
        depends_on, attributes=self.resource_attributes)
    rest_api.BinaryMediaTypes = self.binary_media
    rest_api.MinimumCompressionSize = self.minimum_compression_size
    if self.endpoint_configuration:
        self._set_endpoint_configuration(rest_api, self.endpoint_configuration)
    elif not RegionConfiguration.is_apigw_edge_configuration_supported():
        self._set_endpoint_configuration(rest_api, 'REGIONAL')
    if self.definition_uri and self.definition_body:
        raise InvalidResourceException(self.logical_id,
            "Specify either 'DefinitionUri' or 'DefinitionBody' property and not both"
            )
    self._add_cors()
    self._add_auth()
    self._add_gateway_responses()
    if self.definition_uri:
        rest_api.BodyS3Location = self._construct_body_s3_dict()
    elif self.definition_body:
        rest_api.Body = self.definition_body
    if self.name:
        rest_api.Name = self.name
    return rest_api