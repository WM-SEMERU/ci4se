def find_behind_subscriptions():
    subscriptions = Subscription.objects.filter(active=True, completed=
        False, process_status=0).values_list('id', flat=True)
    for subscription_id in subscriptions.iterator():
        calculate_subscription_lifecycle.delay(str(subscription_id))