def _compare_acl(current, desired, region, key, keyid, profile):
    ocid = _get_canonical_id(region, key, keyid, profile)
    return __utils__['boto3.json_objs_equal'](current, _acl_to_grant(
        desired, ocid))