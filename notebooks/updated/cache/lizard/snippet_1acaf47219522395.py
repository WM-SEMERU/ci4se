def endpoint_from_model_data(self, model_s3_location, deployment_image,
    initial_instance_count, instance_type, name=None, role=None, wait=True,
    model_environment_vars=None, model_vpc_config=None, accelerator_type=None):
    model_environment_vars = model_environment_vars or {}
    name = name or name_from_image(deployment_image)
    model_vpc_config = vpc_utils.sanitize(model_vpc_config)
    if _deployment_entity_exists(lambda : self.sagemaker_client.
        describe_endpoint(EndpointName=name)):
        raise ValueError(
            'Endpoint with name "{}" already exists; please pick a different name.'
            .format(name))
    if not _deployment_entity_exists(lambda : self.sagemaker_client.
        describe_model(ModelName=name)):
        primary_container = container_def(image=deployment_image,
            model_data_url=model_s3_location, env=model_environment_vars)
        self.create_model(name=name, role=role, container_defs=
            primary_container, vpc_config=model_vpc_config)
    if not _deployment_entity_exists(lambda : self.sagemaker_client.
        describe_endpoint_config(EndpointConfigName=name)):
        self.create_endpoint_config(name=name, model_name=name,
            initial_instance_count=initial_instance_count, instance_type=
            instance_type, accelerator_type=accelerator_type)
    self.create_endpoint(endpoint_name=name, config_name=name, wait=wait)
    return name