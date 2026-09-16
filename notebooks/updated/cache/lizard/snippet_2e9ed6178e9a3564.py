def write_case_data(self, file):
    writer = self._get_writer(file)
    writer.writerow(['Name', 'base_mva'])
    writer.writerow([self.case.name, self.case.base_mva])