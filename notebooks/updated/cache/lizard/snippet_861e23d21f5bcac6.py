def print_xmlsec_errors(filename, line, func, error_object, error_subject,
    reason, msg):
    info = []
    if error_object != 'unknown':
        info.append('obj=' + error_object)
    if error_subject != 'unknown':
        info.append('subject=' + error_subject)
    if msg.strip():
        info.append('msg=' + msg)
    if reason != 1:
        info.append('errno=%d' % reason)
    if info:
        print('%s:%d(%s)' % (filename, line, func), ' '.join(info))