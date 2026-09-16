def folder_get_info(self, folder_key=None, device_id=None, details=None):
    return self.request('folder/get_info', QueryParams({'folder_key':
        folder_key, 'device_id': device_id, 'details': details}))