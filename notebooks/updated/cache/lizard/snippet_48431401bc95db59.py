def get_plan_table(self, plan_list):
    quota_list = Quota.objects.all().filter(planquota__plan__in=plan_list
        ).distinct()
    plan_quotas_dic = {}
    for plan in plan_list:
        plan_quotas_dic[plan] = {}
        for plan_quota in plan.planquota_set.all():
            plan_quotas_dic[plan][plan_quota.quota] = plan_quota
    return map(lambda quota: (quota, map(lambda plan: plan_quotas_dic[plan]
        .get(quota, None), plan_list)), quota_list)