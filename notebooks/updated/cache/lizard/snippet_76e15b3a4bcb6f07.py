def get_folder_by_id(self, folder_id):
    return self._create_item_response(self.data_service.get_folder(
        folder_id), Folder)