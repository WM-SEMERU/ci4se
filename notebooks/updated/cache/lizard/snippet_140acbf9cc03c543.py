def process_upload(self, set_content_type=True):
    metadata = self.get_upload_key_metadata()
    if set_content_type:
        content_type = self.get_upload_content_type()
        metadata.update({b'Content-Type': b'{0}'.format(content_type)})
    upload_key = self.get_upload_key()
    processed_key_name = self.get_processed_key_name()
    processed_key = upload_key.copy(upload_key.bucket.name,
        processed_key_name, metadata)
    processed_key.set_acl(self.get_processed_acl())
    upload_key.delete()
    return processed_key