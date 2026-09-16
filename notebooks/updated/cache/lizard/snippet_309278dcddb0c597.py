def addProfile(self, profile):
    if profile in self._profiles:
        return
    self._profiles.append(profile)
    self._profileCombo.blockSignals(True)
    self._profileCombo.addItem(profile.name())
    self._profileCombo.setCurrentIndex(self._profileCombo.count() - 1)
    self._profileCombo.blockSignals(False)