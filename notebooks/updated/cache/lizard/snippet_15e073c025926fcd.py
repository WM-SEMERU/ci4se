def put(self):
    return self.manager.put(id=self.id, name=self.name, description=self.
        description, command_to_run=self.command_to_run,
        environment_variables=self.environment_variables,
        required_arguments=self.required_arguments,
        required_arguments_default_values=self.
        required_arguments_default_values, logs_path=self.logs_path,
        results_path=self.results_path, container_image=self.
        container_image, container_type=self.container_type)