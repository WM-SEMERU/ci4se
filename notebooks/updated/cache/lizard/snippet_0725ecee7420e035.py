def set_folder_names(self, folder_names):
    assert self.root_path is not None
    path_list = [osp.join(self.root_path, dirname) for dirname in folder_names]
    self.proxymodel.setup_filter(self.root_path, path_list)