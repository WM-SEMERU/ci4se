def is_crm_dc():
    cmd = ['crm', 'status']
    try:
        status = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        if not isinstance(status, six.text_type):
            status = six.text_type(status, 'utf-8')
    except subprocess.CalledProcessError as ex:
        raise CRMDCNotFound(str(ex))
    current_dc = ''
    for line in status.split('\n'):
        if line.startswith('Current DC'):
            current_dc = line.split(':')[1].split()[0]
    if current_dc == get_unit_hostname():
        return True
    elif current_dc == 'NONE':
        raise CRMDCNotFound('Current DC: NONE')
    return False