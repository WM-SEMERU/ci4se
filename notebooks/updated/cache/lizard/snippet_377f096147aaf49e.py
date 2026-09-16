def complete(self, table_name, key):
    job_key = dict(table_name=table_name, key_hash=key_hash(key))
    (self & job_key).delete_quick()