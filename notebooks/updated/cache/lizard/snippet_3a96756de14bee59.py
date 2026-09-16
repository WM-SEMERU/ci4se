def find(format):
    try:
        serializer = SERIALIZERS[format]
    except KeyError:
        raise UnknownSerializer('No serializer found for %s' % format.acronym)
    return serializer