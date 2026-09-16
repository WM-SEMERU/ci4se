def create_resource_model_instance(resource_instance):
    resource_model = ResourceModelParser.get_resource_model(resource_instance)
    resource_class_name = ResourceModelParser.get_resource_model_class_name(
        resource_model)
    instance = ResourceModelParser.get_class(
        'cloudshell.cp.vcenter.models.' + resource_class_name)
    return instance