def _load_scratch_orgs(self):
    current_orgs = self.list_orgs()
    if not self.project_config.orgs__scratch:
        return
    for config_name in self.project_config.orgs__scratch.keys():
        if config_name in current_orgs:
            continue
        self.create_scratch_org(config_name, config_name)