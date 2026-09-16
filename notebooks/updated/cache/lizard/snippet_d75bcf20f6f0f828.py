def save_minions(jid, minions, syndic_id=None):
    cb_ = _get_connection()
    try:
        jid_doc = cb_.get(six.text_type(jid))
    except couchbase.exceptions.NotFoundError:
        log.warning('Could not write job cache file for jid: %s', jid)
        return False
    if 'minions' in jid_doc.value:
        jid_doc.value['minions'] = sorted(set(jid_doc.value['minions'] +
            minions))
    else:
        jid_doc.value['minions'] = minions
    cb_.replace(six.text_type(jid), jid_doc.value, cas=jid_doc.cas, ttl=
        _get_ttl())