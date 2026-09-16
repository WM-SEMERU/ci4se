def RemoveKeywordsForName(self, name, keywords):
    data_store.DB.IndexRemoveKeywordsForName(self.urn, name, keywords)