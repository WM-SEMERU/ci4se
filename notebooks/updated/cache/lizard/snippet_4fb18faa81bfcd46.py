def set_Name(self, Name, SaveName=None, include=None, ForceUpdate=False):
    self._dall['Name'] = Name
    self.set_SaveName(SaveName=SaveName, include=include, ForceUpdate=
        ForceUpdate)