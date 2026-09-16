def add_artifact(self, artifact):
    if not issubclass(artifact.__class__, Artifact):
        raise TypeError('Artifact to add ({}) is not {}.'.format(artifact,
            Artifact))
    self._A.append(artifact)