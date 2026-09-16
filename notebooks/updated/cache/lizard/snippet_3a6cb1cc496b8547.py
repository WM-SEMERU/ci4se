def SaveAvatarToFile(self, Filename, AvatarId=1):
    s = 'AVATAR %s %s' % (AvatarId, path2unicode(Filename))
    self._Skype._DoCommand('GET %s' % s, s)