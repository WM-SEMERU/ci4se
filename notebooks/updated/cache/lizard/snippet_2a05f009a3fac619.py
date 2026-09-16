def FromEvent(cls, service_event):
    _, _, name = service_event.key_path.rpartition(WindowsService.
        _REGISTRY_KEY_PATH_SEPARATOR)
    service_type = service_event.regvalue.get('Type', '')
    image_path = service_event.regvalue.get('ImagePath', '')
    start_type = service_event.regvalue.get('Start', '')
    service_dll = service_event.regvalue.get('ServiceDll', '')
    object_name = service_event.regvalue.get('ObjectName', '')
    if service_event.pathspec:
        source = service_event.pathspec.location, service_event.key_path
    else:
        source = 'Unknown', 'Unknown'
    return cls(name=name, service_type=service_type, image_path=image_path,
        start_type=start_type, object_name=object_name, source=source,
        service_dll=service_dll)