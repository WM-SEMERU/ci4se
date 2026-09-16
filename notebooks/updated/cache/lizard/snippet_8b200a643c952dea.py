def addFeatureSet(self):
    self._openRepo()
    dataset = self._repo.getDatasetByName(self._args.datasetName)
    filePath = self._getFilePath(self._args.filePath, self._args.relativePath)
    name = getNameFromPath(self._args.filePath)
    featureSet = sequence_annotations.Gff3DbFeatureSet(dataset, name)
    referenceSetName = self._args.referenceSetName
    if referenceSetName is None:
        raise exceptions.RepoManagerException(
            'A reference set name must be provided')
    referenceSet = self._repo.getReferenceSetByName(referenceSetName)
    featureSet.setReferenceSet(referenceSet)
    ontologyName = self._args.ontologyName
    if ontologyName is None:
        raise exceptions.RepoManagerException(
            'A sequence ontology name must be provided')
    ontology = self._repo.getOntologyByName(ontologyName)
    self._checkSequenceOntology(ontology)
    featureSet.setOntology(ontology)
    featureSet.populateFromFile(filePath)
    featureSet.setAttributes(json.loads(self._args.attributes))
    self._updateRepo(self._repo.insertFeatureSet, featureSet)