def _set_upload_status(self, file_data_object, upload_status):
    uuid = file_data_object['uuid']
    return self.connection.update_data_object(uuid, {'uuid': uuid, 'value':
        {'upload_status': upload_status}})