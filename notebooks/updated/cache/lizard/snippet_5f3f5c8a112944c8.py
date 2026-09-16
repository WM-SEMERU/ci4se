def get_notifications(self, startDate, endDate, loadBalancerID,
    loadBalancerRuleID):
    return self._call(GetLoadBalancerNotifications, startDate=startDate,
        endDate=endDate, loadBalancerID=loadBalancerID, loadBalancerRuleID=
        loadBalancerRuleID)