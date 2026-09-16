def set_data(self, frames):
    data_frames = []
    for frame in frames:
        frame = frame.swapaxes(0, 1)
        if len(frame.shape) < 3:
            frame = np.array([frame]).swapaxes(0, 2).swapaxes(0, 1)
        data_frames.append(frame)
    frames_n = len(data_frames)
    data_frames = np.array(data_frames)
    data_frames = np.rollaxis(data_frames, 3)
    data_frames = data_frames.swapaxes(2, 3)
    self.data = data_frames
    self.length = frames_n