def setProfile(self, profile):
    self._profile = profile
    self.setIcon(profile.icon())
    self.setText(profile.name())
    self.setToolTip(profile.description())