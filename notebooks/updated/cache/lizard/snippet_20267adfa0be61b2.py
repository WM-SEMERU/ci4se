def _SetGuide(self, guideName):
    if guideName == epguides.EPGuidesLookup.GUIDE_NAME:
        self._guide = epguides.EPGuidesLookup()
    else:
        raise Exception(
            '[RENAMER] Unknown guide set for TVRenamer selection: Got {}, Expected {}'
            .format(guideName, epguides.EPGuidesLookup.GUIDE_NAME))