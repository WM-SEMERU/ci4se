def toggle_use_font_background_sensitivity(self, chk):
    self.get_widget('palette_16').set_sensitive(chk.get_active())
    self.get_widget('palette_17').set_sensitive(chk.get_active())