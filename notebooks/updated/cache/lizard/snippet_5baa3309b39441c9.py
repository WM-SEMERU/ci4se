def insertCallSet(self, callSet):
    try:
        models.Callset.create(id=callSet.getId(), name=callSet.getLocalId(),
            variantsetid=callSet.getParentContainer().getId(), biosampleid=
            callSet.getBiosampleId(), attributes=json.dumps(callSet.
            getAttributes()))
    except Exception as e:
        raise exceptions.RepoManagerException(e)