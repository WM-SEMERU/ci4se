def addVariantSet(self, variantSet):
    id_ = variantSet.getId()
    self._variantSetIdMap[id_] = variantSet
    self._variantSetNameMap[variantSet.getLocalId()] = variantSet
    self._variantSetIds.append(id_)