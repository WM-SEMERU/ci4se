async def handle_frame(self, frame):
    if isinstance(frame, FrameActivateSceneConfirmation
        ) and frame.session_id == self.session_id:
        if frame.status == ActivateSceneConfirmationStatus.ACCEPTED:
            self.success = True
        return not self.wait_for_completion
    if isinstance(frame, FrameCommandRemainingTimeNotification
        ) and frame.session_id == self.session_id:
        return False
    if isinstance(frame, FrameCommandRunStatusNotification
        ) and frame.session_id == self.session_id:
        return False
    if isinstance(frame, FrameSessionFinishedNotification
        ) and frame.session_id == self.session_id:
        return True
    return False