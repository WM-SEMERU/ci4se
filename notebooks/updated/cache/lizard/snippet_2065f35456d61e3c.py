def validate_is_document_type(option, value):
    if not isinstance(value, (collections.MutableMapping, RawBSONDocument)):
        raise TypeError(
            '%s must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument, or a type that inherits from collections.MutableMapping'
             % (option,))