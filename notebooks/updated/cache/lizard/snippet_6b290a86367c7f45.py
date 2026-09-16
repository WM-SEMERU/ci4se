def pave_community(self):
    settings.project_config.path.mkdir()
    settings.project_config.base.write_text(self.context.base_text)
    settings.project_config.os_packages.write_text('[]')
    settings.project_config.lang_packages.write_text('{}')