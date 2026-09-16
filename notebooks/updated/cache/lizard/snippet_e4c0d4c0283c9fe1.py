def check_container(self, container_path, container_format=None,
    config_string=None):
    self.log(["Checking container '%s'", container_path])
    self.result = ValidatorResult()
    if self._are_safety_checks_disabled('check_container'):
        return self.result
    if not (gf.file_exists(container_path) or gf.directory_exists(
        container_path)):
        self._failed("Container '%s' not found." % container_path)
        return self.result
    container = Container(container_path, container_format)
    try:
        self.log('Checking container has config file')
        if config_string is not None:
            self.log('Container with config string from wizard')
            self.check_config_txt(config_string, is_config_string=True)
        elif container.has_config_xml:
            self.log('Container has XML config file')
            contents = container.read_entry(container.entry_config_xml)
            if contents is None:
                self._failed('Unable to read the contents of XML config file.')
                return self.result
            self.check_config_xml(contents)
        elif container.has_config_txt:
            self.log('Container has TXT config file')
            contents = container.read_entry(container.entry_config_txt)
            if contents is None:
                self._failed('Unable to read the contents of TXT config file.')
                return self.result
            self.check_config_txt(contents, is_config_string=False)
        else:
            self._failed(
                'Container does not have a TXT or XML configuration file.')
        self.log('Checking we have a valid job in the container')
        if not self.result.passed:
            return self.result
        self.log('Analyze the contents of the container')
        analyzer = AnalyzeContainer(container)
        if config_string is not None:
            job = analyzer.analyze(config_string=config_string)
        else:
            job = analyzer.analyze()
        self._check_analyzed_job(job, container)
    except OSError:
        self._failed('Unable to read the contents of the container.')
    return self.result