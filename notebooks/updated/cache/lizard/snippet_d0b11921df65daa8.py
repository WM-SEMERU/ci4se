def _get_annotation_heading(self, handler, route, heading=None):
    if hasattr(handler, '_doctor_heading'):
        return handler._doctor_heading
    heading = ''
    handler_path = str(handler)
    try:
        handler_file_name = handler_path.split('.')[-2]
    except IndexError:
        handler_file_name = 'handler'
    if handler_file_name.startswith('handler'):
        class_name = handler_path.split('.')[-1]
        internal = False
        for word in CAMEL_CASE_RE.findall(class_name):
            if word == 'Internal':
                internal = True
                continue
            elif word.startswith(('List', 'Handler', 'Resource')):
                break
            heading += '%s ' % (word,)
        if internal:
            heading = heading.strip()
            heading += ' (Internal)'
    else:
        heading = ' '.join(handler_file_name.split('_')).title()
        if 'internal' in route:
            heading += ' (Internal)'
    return heading.strip()