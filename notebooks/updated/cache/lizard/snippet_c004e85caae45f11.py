def create_resource(self, parent_id=''):
    resource_name = self.trigger_settings.get('resource', '')
    resource_name = resource_name.replace('/', '')
    if not self.resource_id:
        created_resource = self.client.create_resource(restApiId=self.
            api_id, parentId=parent_id, pathPart=resource_name)
        self.resource_id = created_resource['id']
        self.log.info('Successfully created resource')
    else:
        self.log.info(
            'Resource already exists. To update resource please delete existing resource: %s'
            , resource_name)