def wrap(self, data, many):
    if not many:
        return data
    else:
        data = {'contents': data}
        bucket = self.context.get('bucket')
        if bucket:
            data.update(BucketSchema().dump(bucket).data)
        return data