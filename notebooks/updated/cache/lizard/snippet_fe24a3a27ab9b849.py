def parse_reports(self):
    data = _parse_reports_by_type(self)
    if data:
        data = self.ignore_samples(data)
        _add_data_to_general_stats(self, data)
        _add_section_to_report(self, data)
        self.write_data_file(data, 'multiqc_picard_validatesamfile')
    self.picard_ValidateSamFile_data = data
    return len(data)