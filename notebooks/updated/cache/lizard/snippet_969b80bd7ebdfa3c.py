def find_identifiers(src):
    if src.endswith('.pdf'):
        totext = subprocess.Popen(['pdftotext', src, '-'], stdout=
            subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    elif src.endswith('.djvu'):
        totext = subprocess.Popen(['djvutxt', src], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, bufsize=1)
    else:
        return None, None
    while totext.poll() is None:
        extract_full = ' '.join([i.decode('utf-8').strip() for i in totext.
            stdout.readlines()])
        for identifier in __valid_identifiers__:
            module = sys.modules.get('libbmc.%s' % (identifier,), None)
            if module is None:
                continue
            found_id = getattr(module, 'extract_from_text')(extract_full)
            if found_id:
                totext.terminate()
                return identifier, found_id[0]
    return None, None