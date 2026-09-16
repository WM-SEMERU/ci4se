def parse(self):
    self.clean_name = formatter.apply_replacements(self.name, cfg.CONF.
        input_filename_replacements)
    output = parser.parse_filename(self.clean_name)
    if output is None:
        self.messages.append('Invalid filename: unable to parse {0}'.format
            (self.clean_name))
        LOG.info(self.messages[-1])
        raise exc.InvalidFilename(self.messages[-1])
    self.episode_numbers = output.get('episode_numbers')
    if self.episode_numbers is None:
        self.messages.append(
            """Regex does not contain episode number group, should contain episodenumber, episodenumber1-9, or episodenumberstart and episodenumberend

Pattern was:
"""
             + output.get('pattern'))
        LOG.info(self.messages[-1])
        raise exc.ConfigValueError(self.messages[-1])
    self.series_name = output.get('series_name')
    if self.series_name is None:
        self.messages.append(
            'Regex must contain seriesname. Pattern was:\n' + output.get(
            'pattern'))
        LOG.info(self.messages[-1])
        raise exc.ConfigValueError(self.messages[-1])
    self.series_name = formatter.clean_series_name(self.series_name)
    self.season_number = output.get('season_number')