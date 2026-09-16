def parse_gc_content(self):
    for f in self.find_log_files('homer/GCcontent', filehandles=True):
        s_name = os.path.basename(f['root'])
        s_name = self.clean_s_name(s_name, f['root'])
        parsed_data = self.parse_twoCol_file(f)
        if parsed_data is not None:
            if s_name in self.tagdir_data['GCcontent']:
                log.debug(
                    'Duplicate GCcontent sample log found! Overwriting: {}'
                    .format(s_name))
            self.add_data_source(f, s_name, section='GCcontent')
            self.tagdir_data['GCcontent'][s_name] = parsed_data
    for f in self.find_log_files('homer/genomeGCcontent', filehandles=True):
        parsed_data = self.parse_twoCol_file(f)
        if parsed_data is not None:
            if s_name + '_genome' in self.tagdir_data['GCcontent']:
                log.debug(
                    'Duplicate genome GCcontent sample log found! Overwriting: {}'
                    .format(s_name + '_genome'))
            self.add_data_source(f, s_name + '_genome', section='GCcontent')
            self.tagdir_data['GCcontent'][s_name + '_genome'] = parsed_data
    self.tagdir_data['GCcontent'] = self.ignore_samples(self.tagdir_data[
        'GCcontent'])
    if len(self.tagdir_data['GCcontent']) > 0:
        self.add_section(name='Per Sequence GC Content', anchor=
            'homer_per_sequence_gc_content', description=
            'This plot shows the distribution of GC content.', plot=self.
            GCcontent_plot())