def update_one(self, filter, update, upsert=False,
    bypass_document_validation=False, collation=None):
    common.validate_is_mapping('filter', filter)
    common.validate_ok_for_update(update)
    with self._socket_for_writes() as sock_info:
        result = self._update(sock_info, filter, update, upsert, check_keys
            =False, bypass_doc_val=bypass_document_validation, collation=
            collation)
    return UpdateResult(result, self.write_concern.acknowledged)