def grab_focus(self):
    scene = self.get_scene()
    if scene and scene._focus_sprite != self:
        scene._focus_sprite = self