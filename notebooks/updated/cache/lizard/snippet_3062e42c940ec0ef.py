def delete_one(self, *args, **kwargs):
    result = self.collection.delete_one(*args, **kwargs)
    return result.raw_result