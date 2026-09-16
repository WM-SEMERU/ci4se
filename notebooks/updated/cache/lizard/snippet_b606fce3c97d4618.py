def json_integrity(baseline, suspect):
    try:
        for k, v in baseline.items():
            for ks, vs in suspect.items():
                keys_baseline = set(v.keys())
                keys_suspect = set(vs.keys())
                intersect_keys = keys_baseline.intersection(keys_suspect)
                added = keys_baseline - keys_suspect
                rm = keys_suspect - keys_baseline
                logger.info('keys added: %s, keys removed %s' % (str(added),
                    str(rm)))
                if keys_baseline != keys_suspect:
                    return False
    except KeyError as e:
        logger.info(
            'KeyError parsing pre-existing config (%s). Replacing config file'
             % str(e))
    return True