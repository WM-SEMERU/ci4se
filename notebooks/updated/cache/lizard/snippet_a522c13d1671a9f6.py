def EvalGeneric(self, hashers=None):
    if hashers is None:
        hashers = Fingerprinter.GENERIC_HASH_CLASSES
    hashfuncs = [x() for x in hashers]
    finger = Finger(hashfuncs, [Range(0, self.filelength)], {'name': 'generic'}
        )
    self.fingers.append(finger)
    return True