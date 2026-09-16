def get_sample(self, md5):
    sample = self.data_store.get_sample(md5)
    if not sample:
        return {'sample_set': {'md5_list': self.get_sample_set(md5)}}
    return {'sample': sample}