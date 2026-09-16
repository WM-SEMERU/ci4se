def Deserializer(stream_or_string, **options):
    if isinstance(stream_or_string, (bytes, six.string_types)):
        stream_or_string = BytesIO(stream_or_string)
    try:

        def line_generator():
            for line in stream_or_string:
                yield json.loads(line.strip())
        for obj in PythonDeserializer(line_generator(), **options):
            yield obj
    except GeneratorExit:
        raise
    except Exception as e:
        six.reraise(DeserializationError, DeserializationError(e), sys.
            exc_info()[2])