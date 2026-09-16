def get_last_scene_id(self, refresh=False):
    if refresh:
        self.refresh_complex_value('LastSceneID')
        self.refresh_complex_value('sl_CentralScene')
    val = self.get_complex_value('LastSceneID') or self.get_complex_value(
        'sl_CentralScene')
    return val