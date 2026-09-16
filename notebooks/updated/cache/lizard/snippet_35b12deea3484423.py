def download_and_transform_file(self, path):
    key = 'DOWNLOAD:{}'.format(path)
    if not config.UPDATE and FILECACHE.get(key):
        return FILECACHE.get(key).decode('utf-8')
    config.LOGGER.info('\tDownloading {}'.format(path))
    if self.subtitlesformat == file_formats.VTT:
        with tempfile.TemporaryFile() as tempf:
            hash = write_and_get_hash(path, tempf)
            tempf.seek(0)
            filename = '{0}.{ext}'.format(hash.hexdigest(), ext=self.
                default_ext)
            copy_file_to_storage(filename, tempf)
            FILECACHE.set(key, bytes(filename, 'utf-8'))
    elif self.subtitlesformat == file_formats.SRT:
        with tempfile.NamedTemporaryFile(
            ) as tempf_srt, tempfile.NamedTemporaryFile() as tempf_vtt:
            hash_srt = write_and_get_hash(path, tempf_srt)
            tempf_srt.seek(0)
            filename_tmp_vtt = os.path.join('/tmp', '{0}.{ext}'.format(
                hash_srt.hexdigest(), ext=self.default_ext))
            error_msg = srt2vtt(tempf_srt.name, filename_tmp_vtt)
            hash = write_and_get_hash(filename_tmp_vtt, tempf_vtt)
            tempf_vtt.seek(0)
            filename = '{0}.{ext}'.format(hash.hexdigest(), ext=self.
                default_ext)
            copy_file_to_storage(filename, tempf_vtt.name)
            if error_msg is not None:
                config.LOGGER.error(' An Error found in ' + path)
                config.LOGGER.error(error_msg)
            else:
                FILECACHE.set(key, bytes(filename, 'utf-8'))
    return filename