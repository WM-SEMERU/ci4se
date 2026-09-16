def _GetResourceTimestamps(self, pefile_object):
    timestamps = []
    if not hasattr(pefile_object, 'DIRECTORY_ENTRY_RESOURCE'):
        return timestamps
    for entrydata in pefile_object.DIRECTORY_ENTRY_RESOURCE.entries:
        directory = entrydata.directory
        timestamp = getattr(directory, 'TimeDateStamp', 0)
        if timestamp:
            timestamps.append(timestamp)
    return timestamps