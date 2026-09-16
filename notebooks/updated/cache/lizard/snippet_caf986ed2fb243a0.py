def GetTopLevel(self, file_object):
    try:
        top_level_object = biplist.readPlist(file_object)
    except (biplist.InvalidPlistException, biplist.NotBinaryPlistException
        ) as exception:
        raise errors.UnableToParseFile(
            'Unable to parse plist with error: {0!s}'.format(exception))
    return top_level_object