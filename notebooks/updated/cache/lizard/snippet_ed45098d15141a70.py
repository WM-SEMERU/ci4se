def getAnalysisServiceSettings(self, uid):
    sets = [s for s in self.getAnalysisServicesSettings() if s.get('uid',
        '') == uid]
    if not sets and self.getTemplate():
        adv = self.getTemplate().getAnalysisServiceSettings(uid)
        sets = [adv] if 'hidden' in adv else []
    if not sets and self.getProfiles():
        adv = []
        adv += [profile.getAnalysisServiceSettings(uid) for profile in self
            .getProfiles()]
        sets = adv if 'hidden' in adv[0] else []
    return sets[0] if sets else {'uid': uid}