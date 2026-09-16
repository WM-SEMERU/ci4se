def set_camera_enabled(self, camera_id, is_enabled):
    self.publish(action='set', resource='privacy', camera_id=camera_id,
        mode=is_enabled, publish_response=True)
    self.update()