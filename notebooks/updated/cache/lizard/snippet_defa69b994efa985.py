def __get_value(self, bundleId, languageId, resourceKey, fallback=False):
    resourceEntryData = self.__get_resource_entry_data(bundleId=bundleId,
        languageId=languageId, resourceKey=resourceKey, fallback=fallback)
    if not resourceEntryData:
        return None
    value = resourceEntryData.get(self.__RESPONSE_TRANSLATION_KEY)
    return value