def get_file_versions(self, secure_data_path, limit=None, offset=None):
    return self.get_secret_versions(secure_data_path, limit, offset)