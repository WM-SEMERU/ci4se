def delete_folders(self, paths=None, folder_ids=None, f_type='folder'):
    if folder_ids:
        f_ids = folder_ids
    elif paths:
        f_ids = []
        for path in paths:
            folder = self.get_folder(path=path)
            f_ids.append(folder[f_type]['id'])
    comma_ids = self._return_comma_list(f_ids)
    params = {'action': {'id': comma_ids, 'op': 'delete'}}
    self.request('FolderAction', params)