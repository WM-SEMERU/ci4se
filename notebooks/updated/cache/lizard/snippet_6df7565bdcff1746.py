def get_blob(self, blob_name, client=None, encryption_key=None, generation=
    None, **kwargs):
    blob = Blob(bucket=self, name=blob_name, encryption_key=encryption_key,
        generation=generation, **kwargs)
    try:
        blob.reload(client=client)
    except NotFound:
        return None
    else:
        return blob