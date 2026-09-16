def validate(self):
    from .files import VideoFile, WebVideoFile
    try:
        assert self.kind == content_kinds.VIDEO, 'Assumption Failed: Node should be a video'
        assert self.questions == [
            ], 'Assumption Failed: Video should not have questions'
        assert len(self.files
            ) > 0, 'Assumption Failed: Video must have at least one video file'
        assert any(f for f in self.files if isinstance(f, VideoFile) or
            isinstance(f, WebVideoFile)
            ), 'Assumption Failed: Video should have at least one .mp4 file'
        return super(VideoNode, self).validate()
    except AssertionError as ae:
        raise InvalidNodeException('Invalid node ({}): {} - {}'.format(ae.
            args[0], self.title, self.__dict__))