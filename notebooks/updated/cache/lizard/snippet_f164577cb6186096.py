def _walk(self, root_path=''):
    title = '%s._walk' % self.__class__.__name__
    if root_path:
        root_path = '/%s' % root_path
    try:
        response = self.dropbox.files_list_folder(path=root_path, recursive
            =True)
        for record in response.entries:
            if not isinstance(record, self.objects.FileMetadata):
                continue
            yield record.path_display[1:]
        if response.has_more:
            while response.has_more:
                response = self.dropbox.files_list_folder_continue(response
                    .cursor)
                for record in response.entries:
                    if not isinstance(record, self.objects.FileMetadata):
                        continue
                    yield record.path_display[1:]
    except:
        raise DropboxConnectionError(title)