def active_subscriptions(self):
    return self.subscriptions.filter(status=enums.SubscriptionStatus.active,
        current_period_end__gt=timezone.now())