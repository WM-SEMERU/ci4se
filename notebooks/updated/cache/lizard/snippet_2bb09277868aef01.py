def run(self):
    try:
        self.hide_files = get_hide_files(self.workflow)
    except KeyError:
        self.log.info('Skipping hide files: no files to hide')
        return
    self._populate_start_file_lines()
    self._populate_end_file_lines()
    self.dfp = df_parser(self.workflow.builder.df_path)
    stages = self._find_stages()
    for stage in reversed(stages):
        self._update_dockerfile(**stage)