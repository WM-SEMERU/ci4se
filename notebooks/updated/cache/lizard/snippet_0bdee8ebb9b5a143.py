def add_subproject(self, fname, conf_path):
    config = Config(conf_file=conf_path)
    proj = Project(self.app, dependency_map=self.dependency_map)
    proj.parse_name_from_config(config)
    proj.parse_config(config)
    proj.setup()
    self.subprojects[fname] = proj