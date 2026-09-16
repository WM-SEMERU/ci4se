def get_file_suffix(self, path, prefix):
    parent = self._ensure_folder_path(path)
    file_list = self.drive.ListFile({'q':
        "'{}' in parents and trashed=false and title contains '{}'".format(
        parent['id'], prefix)}).GetList()
    try:
        number_of_files = len(file_list)
    except:
        number_of_files = 0
    return '{0:04}'.format(number_of_files)