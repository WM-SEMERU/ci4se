def AddClient(self, client):
    keywords = self.AnalyzeClient(client)
    keywords.add(self._NormalizeKeyword(client.client_id))
    data_store.REL_DB.AddClientKeywords(client.client_id, keywords)