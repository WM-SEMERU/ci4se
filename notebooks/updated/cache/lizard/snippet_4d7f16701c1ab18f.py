def removeReferenceSet(self, referenceSet):
    try:
        q = models.Reference.delete().where(models.Reference.referencesetid ==
            referenceSet.getId())
        q.execute()
        q = models.Referenceset.delete().where(models.Referenceset.id ==
            referenceSet.getId())
        q.execute()
    except Exception:
        msg = (
            'Unable to delete reference set.  There are objects currently in the registry which are aligned against it.  Remove these objects before removing the reference set.'
            )
        raise exceptions.RepoManagerException(msg)