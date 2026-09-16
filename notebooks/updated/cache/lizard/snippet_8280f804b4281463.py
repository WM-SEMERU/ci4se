def calling_convention(self):
    if self._calling_convention is None:
        self._calling_convention = (calldef_types.CALLING_CONVENTION_TYPES.
            extract(self.attributes))
        if not self._calling_convention:
            self._calling_convention = self.guess_calling_convention()
    return self._calling_convention