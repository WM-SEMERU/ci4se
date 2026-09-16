def _get_service_config(self):
    if not os.path.exists(self.config_path):
        try:
            os.makedirs(os.path.dirname(self.config_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
        return {}
    with open(self.config_path, 'r') as data:
        return json.load(data)