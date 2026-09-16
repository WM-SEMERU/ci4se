def __get_language_data(self, bundleId, languageId, fallback=False):
    url = self.__get_base_bundle_url() + '/' + bundleId + '/' + languageId
    params = {'fallback': 'true'} if fallback else None
    response = self.__perform_rest_call(requestURL=url, params=params)
    if not response:
        return None
    languageData = response.get(self.__RESPONSE_RESOURCE_STRINGS_KEY)
    return languageData