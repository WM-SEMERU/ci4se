def collect_hunt_results(self, hunt):
    if not os.path.isdir(self.output_path):
        os.makedirs(self.output_path)
    output_file_path = os.path.join(self.output_path, '.'.join((self.
        hunt_id, 'zip')))
    if os.path.exists(output_file_path):
        print('{0:s} already exists: Skipping'.format(output_file_path))
        return None
    self._check_approval_wrapper(hunt, self._get_and_write_archive, hunt,
        output_file_path)
    results = self._extract_hunt_results(output_file_path)
    print('Wrote results of {0:s} to {1:s}'.format(hunt.hunt_id,
        output_file_path))
    return results