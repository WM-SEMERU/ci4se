def get_yaml_files_at_env_root(self):
    yaml_files = glob.glob(os.path.join(self.env_root, '*.yaml'))
    yml_files = glob.glob(os.path.join(self.env_root, '*.yml'))
    return yaml_files + yml_files