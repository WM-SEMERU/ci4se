def download_archive_artifact_bundle(self, id_or_uri, file_path):
    uri = self.BACKUP_ARCHIVE_PATH + '/' + extract_id_from_uri(id_or_uri)
    return self._client.download(uri, file_path)