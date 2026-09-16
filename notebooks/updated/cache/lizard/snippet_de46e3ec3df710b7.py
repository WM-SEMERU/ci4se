def delete_vector(self, hash_name, bucket_keys, data):
    for key in bucket_keys:
        bucket = self.get_bucket(hash_name, key)
        bucket[:] = [(v, id_data) for v, id_data in bucket if id_data != data]