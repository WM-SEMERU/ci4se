def _create_resource_group(self, region, resource_group_name):
    resource_group_config = {'location': region}
    try:
        self.resource.resource_groups.create_or_update(resource_group_name,
            resource_group_config)
    except Exception as error:
        raise AzureCloudException('Unable to create resource group: {0}.'.
            format(error))