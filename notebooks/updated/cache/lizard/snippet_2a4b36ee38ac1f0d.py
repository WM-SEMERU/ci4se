def convert_in_oid(service_name):
    s = service_name
    service_ascii = [ord(c) for c in s]
    length = str(len(s))
    oid = base_oid + '.' + length + '.' + '.'.join(str(x) for x in
        service_ascii)
    return oid