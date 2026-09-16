def ScanByType(self, type_name, after_timestamp=None, include_suffix=False,
    max_records=None):
    sub_collection_urn = self.collection_id.Add(type_name)
    sub_collection = sequential_collection.GrrMessageCollection(
        sub_collection_urn)
    for item in sub_collection.Scan(after_timestamp=after_timestamp,
        include_suffix=include_suffix, max_records=max_records):
        yield item