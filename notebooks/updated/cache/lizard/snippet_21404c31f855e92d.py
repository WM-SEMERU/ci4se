def get_files_to_remove(self):
    files_to_remove = {}
    needful_files = self.get_needful_files()
    for resources_type, resources in self.get_uploaded_resources():
        exclude_paths = self.get_exclude_paths()
        resources = {resource for resource in resources if not resource.
            startswith(exclude_paths)}
        files_to_remove[resources_type] = resources - needful_files
    return files_to_remove