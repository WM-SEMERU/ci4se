def create_append_blob_service(self):
    try:
        from azure.storage.blob.appendblobservice import AppendBlobService
        return AppendBlobService(self.account_name, self.account_key,
            sas_token=self.sas_token, is_emulated=self.is_emulated)
    except ImportError:
        raise Exception('The package azure-storage-blob is required. ' +
            'Please install it using "pip install azure-storage-blob"')