def register_serializer(name, serializer):
    if not isclass(serializer):
        serializer = serializer.__class__
    _serializers[name] = serializer