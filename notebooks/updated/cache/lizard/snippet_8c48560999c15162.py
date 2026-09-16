def saveSettings(self, settings):
    settings.beginGroup(self.objectName())
    curr_prof = self.currentProfile()
    if curr_prof:
        settings.setValue('current', curr_prof.name())
    for profile in self.profiles():
        settings.beginGroup(profile.name())
        settings.setValue('profile', wrapVariant(profile.toString()))
        settings.endGroup()
    settings.endGroup()