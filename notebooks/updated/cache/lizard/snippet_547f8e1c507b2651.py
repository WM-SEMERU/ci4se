def _FormatServiceText(self, service):
    string_segments = [service.name, '\tImage Path    = {0:s}'.format(
        service.image_path), '\tService Type  = {0:s}'.format(service.
        HumanReadableType()), '\tStart Type    = {0:s}'.format(service.
        HumanReadableStartType()), '\tService Dll   = {0:s}'.format(service
        .service_dll), '\tObject Name   = {0:s}'.format(service.object_name
        ), '\tSources:']
    for source in service.sources:
        string_segments.append('\t\t{0:s}:{1:s}'.format(source[0], source[1]))
    return '\n'.join(string_segments)