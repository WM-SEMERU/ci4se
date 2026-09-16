def get_output_files(self):
    if self.info is None:
        self.get_info()
    if 'outputFiles' in self.info:
        return [GPFile(self.server_data, f['link']['href']) for f in self.
            info['outputFiles']]
    else:
        return []