async def handle_frame(self, frame):
    if not isinstance(frame, FrameGetVersionConfirmation):
        return False
    self.version = frame.version
    self.success = True
    return True