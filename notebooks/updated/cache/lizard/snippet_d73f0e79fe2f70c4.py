def on_files_dropped_on_group(self, files, group_id: int):
    self.__add_urls_to_group(files, group_id=group_id)