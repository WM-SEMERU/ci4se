def ListChildren(self, limit=None, age=NEWEST_TIME):
    for predicate, timestamp in data_store.DB.AFF4FetchChildren(self.urn,
        timestamp=Factory.ParseAgeSpecification(age), limit=limit):
        urn = self.urn.Add(predicate)
        urn.age = rdfvalue.RDFDatetime(timestamp)
        yield urn