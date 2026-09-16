def _build_autoload_details(self, autoload_data, relative_path=''):
    self._autoload_details.attributes.extend([AutoLoadAttribute(
        relative_address=relative_path, attribute_name=attribute_name,
        attribute_value=attribute_value) for attribute_name,
        attribute_value in autoload_data.attributes.iteritems()])
    for resource_relative_path, resource in self._validate_build_resource_structure(
        autoload_data.resources).iteritems():
        full_relative_path = posixpath.join(relative_path,
            resource_relative_path)
        self._autoload_details.resources.append(AutoLoadResource(model=
            resource.cloudshell_model_name, name=resource.name,
            relative_address=full_relative_path, unique_identifier=resource
            .unique_identifier))
        self._build_autoload_details(autoload_data=resource, relative_path=
            full_relative_path)