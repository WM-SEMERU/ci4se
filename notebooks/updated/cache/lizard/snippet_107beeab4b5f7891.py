def ConvertValues(default_metadata, values, token=None, options=None):
    batch_data = [(default_metadata, obj) for obj in values]
    return ConvertValuesWithMetadata(batch_data, token=token, options=options)