def create_folder(self, folder_name, parent_kind_str, parent_uuid):
    return self._create_item_response(self.data_service.create_folder(
        folder_name, parent_kind_str, parent_uuid), Folder)