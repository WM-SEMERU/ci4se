def _BuildFindSpecsFromGroupName(self, group_name, environment_variables):
    definition = self._artifacts_registry.GetDefinitionByName(group_name)
    if not definition:
        return None
    return self._BuildFindSpecsFromArtifact(definition, environment_variables)