def GetWarnings(self):
    if self._HasAttributeContainers(self._CONTAINER_TYPE_EXTRACTION_ERROR):
        return self._GetExtractionErrorsAsWarnings()
    return self._GetAttributeContainers(self._CONTAINER_TYPE_EXTRACTION_WARNING
        )