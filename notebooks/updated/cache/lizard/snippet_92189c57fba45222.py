def remove_sbi_id(self, sbi_id):
    sbi_ids = self.sbi_ids
    sbi_ids.remove(sbi_id)
    DB.set_hash_value(self._key, 'sbi_ids', sbi_ids)