def _get_package_status(package):
    status = package['status_str'] or 'Unknown'
    stage = package['stage_str'] or 'Unknown'
    if stage == 'Fully Synchronised':
        return status
    return '%(status)s / %(stage)s' % {'status': status, 'stage': stage}