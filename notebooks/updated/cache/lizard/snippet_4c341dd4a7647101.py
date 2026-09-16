def update_from_env_namespace(self, namespace):
    self.update(ConfigLoader(os.environ).namespace(namespace))