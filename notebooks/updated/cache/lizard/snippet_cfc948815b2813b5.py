def check_subdomain_transition(cls, existing_subrec, new_subrec):
    if existing_subrec.get_fqn() != new_subrec.get_fqn():
        return False
    if existing_subrec.n + 1 != new_subrec.n:
        return False
    if not new_subrec.verify_signature(existing_subrec.address):
        log.debug('Invalid signature from {}'.format(existing_subrec.address))
        return False
    if virtualchain.address_reencode(existing_subrec.address
        ) != virtualchain.address_reencode(new_subrec.address):
        if new_subrec.independent:
            log.debug('Transfer is independent of domain: {}'.format(
                new_subrec))
            return False
    return True