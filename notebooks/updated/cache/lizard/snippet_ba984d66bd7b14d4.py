def download_current_dataset(self, dest_path='.', dest_filename=None, unzip
    =True, tournament=1):
    if dest_filename is None:
        round_number = self.get_current_round()
        dest_filename = 'numerai_dataset_{0}.zip'.format(round_number)
    elif unzip and not dest_filename.endswith('.zip'):
        dest_filename += '.zip'
    dataset_path = os.path.join(dest_path, dest_filename)
    if os.path.exists(dataset_path):
        self.logger.info('target file already exists')
        return dataset_path
    utils.ensure_directory_exists(dest_path)
    url = self.get_dataset_url(tournament)
    utils.download_file(url, dataset_path, self.show_progress_bars)
    if unzip:
        dataset_name = dest_filename[:-4]
        self._unzip_file(dataset_path, dest_path, dataset_name)
    return dataset_path