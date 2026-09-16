def phoncontent(self, cls='current', correctionhandling=CorrectionHandling.
    CURRENT):
    if not self.SPEAKABLE:
        raise NoSuchPhon
    for e in self:
        if isinstance(e, PhonContent):
            if cls is None or e.cls == cls:
                return e
        elif isinstance(e, Correction):
            try:
                return e.phoncontent(cls, correctionhandling)
            except NoSuchPhon:
                pass
    raise NoSuchPhon