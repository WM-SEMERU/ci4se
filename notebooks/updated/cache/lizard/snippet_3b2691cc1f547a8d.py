def to_object(self, data):
    if not isinstance(data, Data):
        return data
    if is_null_data(data):
        return None
    inp = self._create_data_input(data)
    try:
        type_id = data.get_type()
        serializer = self._registry.serializer_by_type_id(type_id)
        if serializer is None:
            if self._active:
                raise HazelcastSerializationError(
                    'Missing Serializer for type-id:{}'.format(type_id))
            else:
                raise HazelcastInstanceNotActiveError()
        return serializer.read(inp)
    except:
        handle_exception(sys.exc_info()[1], sys.exc_info()[2])
    finally:
        pass