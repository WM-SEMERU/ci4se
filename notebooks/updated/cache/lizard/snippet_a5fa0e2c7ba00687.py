def get_last_scene_time(self, refresh=False):
    if refresh:
        self.refresh_complex_value('LastSceneTime')
    val = self.get_complex_value('LastSceneTime')
    return val