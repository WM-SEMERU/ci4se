def handle_type(self, frames):
    if self.vtype == 'mouth':
        self.process_frames_mouth(frames)
    elif self.vtype == 'face':
        self.process_frames_face(frames)
    else:
        raise Exception('Video type not found')