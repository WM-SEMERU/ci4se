def from_val(val_schema):
    definition = getattr(val_schema, 'definition', val_schema) if isinstance(
        val_schema, BaseSchema) else val_schema
    if isinstance(definition, dict):
        return _dict_to_teleport(definition)
    if isinstance(definition, list):
        if len(definition) == 1:
            return {'Array': from_val(definition[0])}
    if definition in VAL_PRIMITIVES:
        return VAL_PRIMITIVES[definition]
    raise SerializationError('Serializing %r not (yet) supported.' % definition
        )