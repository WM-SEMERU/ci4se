def insertReferenceSet(self, referenceSet):
    try:
        models.Referenceset.create(id=referenceSet.getId(), name=
            referenceSet.getLocalId(), description=referenceSet.
            getDescription(), assemblyid=referenceSet.getAssemblyId(),
            isderived=referenceSet.getIsDerived(), species=json.dumps(
            referenceSet.getSpecies()), md5checksum=referenceSet.
            getMd5Checksum(), sourceaccessions=json.dumps(referenceSet.
            getSourceAccessions()), sourceuri=referenceSet.getSourceUri(),
            dataurl=referenceSet.getDataUrl())
        for reference in referenceSet.getReferences():
            self.insertReference(reference)
    except Exception:
        raise exceptions.DuplicateNameException(referenceSet.getLocalId())