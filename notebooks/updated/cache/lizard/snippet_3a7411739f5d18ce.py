def merge_into_profile_extension(self, profile_extension, record_data,
    match_column, insert_on_no_match, update_on_match):
    profile_extension = profile_extension.get_soap_object(self.client)
    record_data = record_data.get_soap_object(self.client)
    results = self.call('mergeIntoProfileExtension', profile_extension,
        record_data, match_column, insert_on_no_match, update_on_match)
    return [RecipientResult(result) for result in results]