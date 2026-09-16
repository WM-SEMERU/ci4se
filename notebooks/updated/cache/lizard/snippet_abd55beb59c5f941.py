def _get_all_policy_ids(zap_helper):
    policies = zap_helper.zap.ascan.policies()
    return [p['id'] for p in policies]