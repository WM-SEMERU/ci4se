def search_website(self, dom):
    c = CensysWebsites(api_id=self.__uid, api_secret=self.__api_key)
    return c.view(dom)