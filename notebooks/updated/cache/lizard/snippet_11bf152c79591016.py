def process_files(self):
    from .files import VideoFile, ExtractedVideoThumbnailFile, WebVideoFile
    downloaded = super(VideoNode, self).process_files()
    try:
        if self.generate_thumbnail and not self.has_thumbnail():
            videos = [f for f in self.files if isinstance(f, VideoFile) or
                isinstance(f, WebVideoFile)]
            assert len(videos) > 0 and videos[0
                ].filename, 'Cannot extract thumbnail (No videos found on node {0})'.format(
                self.source_id)
            self.set_thumbnail(ExtractedVideoThumbnailFile(config.
                get_storage_path(videos[0].filename)))
            downloaded.append(self.thumbnail.get_filename())
    except AssertionError as ae:
        config.LOGGER.warning(ae)
    return downloaded