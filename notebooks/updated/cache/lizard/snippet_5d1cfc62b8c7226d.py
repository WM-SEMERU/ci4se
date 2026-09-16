def list(gandi, id, altnames, csr, cert, all_status, status, dates, limit):
    options = {'items_per_page': limit}
    if not all_status:
        options['status'] = ['valid', 'pending']
    output_keys = ['cn', 'plan']
    if id:
        output_keys.append('id')
    if status:
        output_keys.append('status')
    if dates:
        output_keys.extend(['date_created', 'date_end'])
    if altnames:
        output_keys.append('altnames')
    if csr:
        output_keys.append('csr')
    if cert:
        output_keys.append('cert')
    result = gandi.certificate.list(options)
    for num, cert in enumerate(result):
        if num:
            gandi.separator_line()
        cert['plan'] = package_desc(gandi, cert['package'])
        output_cert(gandi, cert, output_keys)
    return result