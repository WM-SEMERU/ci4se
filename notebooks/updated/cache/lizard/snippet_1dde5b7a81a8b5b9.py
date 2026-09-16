def _policy_psets(policy_instances):
    if len(policy_instances) == 0:
        return PermissionSet.objects.filter(policyinstance__isnull=True)
    else:
        return PermissionSet.objects.filter(policyinstance__policy__in=
            policy_instances).distinct()