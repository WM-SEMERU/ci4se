def get_data_file_attachment(self, identifier, resource_id):
    model_run = self.get_object(identifier)
    if model_run is None:
        return None, None
    if not resource_id in model_run.attachments:
        return None, None
    attachment = model_run.attachments[resource_id]
    filename = os.path.join(model_run.attachment_directory, resource_id)
    return filename, attachment.mime_type