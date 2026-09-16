def folder_create(self, foldername=None, parent_key=None,
    action_on_duplicate=None, mtime=None):
    return self.request('folder/create', QueryParams({'foldername':
        foldername, 'parent_key': parent_key, 'action_on_duplicate':
        action_on_duplicate, 'mtime': mtime}))