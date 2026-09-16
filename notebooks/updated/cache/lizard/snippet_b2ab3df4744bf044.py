def generate_folder_names(self):
    self.project_dir = os.path.join(prms.Paths.outdatadir, self.project)
    self.batch_dir = os.path.join(self.project_dir, self.name)
    self.raw_dir = os.path.join(self.batch_dir, 'raw_data')