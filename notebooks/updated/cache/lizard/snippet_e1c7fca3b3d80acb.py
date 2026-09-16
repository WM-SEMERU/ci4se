def keepalive(nurse, *patients):
    if DISABLED:
        return
    if hashable(nurse):
        hashable_patients = []
        for p in patients:
            if hashable(p):
                log.debug('Keeping {0} alive for lifetime of {1}'.format(p,
                    nurse))
                hashable_patients.append(p)
            else:
                log.warning(
                    'Unable to keep unhashable object {0} alive for lifetime of {1}'
                    .format(p, nurse))
        KEEPALIVE.setdefault(nurse, set()).update(hashable_patients)
    else:
        log.warning(
            'Unable to keep objects alive for lifetime of unhashable object {0}'
            .format(nurse))