def violations(self, src_path):
    if not any(src_path.endswith(ext) for ext in self.driver.
        supported_extensions):
        return []
    if src_path not in self.violations_dict:
        if self.reports:
            self.violations_dict = self.driver.parse_reports(self.reports)
        else:
            if self.driver_tool_installed is None:
                self.driver_tool_installed = self.driver.installed()
            if not self.driver_tool_installed:
                raise EnvironmentError('{} is not installed'.format(self.
                    driver.name))
            command = copy.deepcopy(self.driver.command)
            if self.options:
                command.append(self.options)
            if os.path.exists(src_path):
                command.append(src_path.encode(sys.getfilesystemencoding()))
                output, _ = execute(command, self.driver.exit_codes)
                self.violations_dict.update(self.driver.parse_reports([output])
                    )
    return self.violations_dict[src_path]