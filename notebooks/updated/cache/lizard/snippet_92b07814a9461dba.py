def calculate_subscription_lifecycle(subscription_id):
    subscription = Subscription.objects.select_related('messageset', 'schedule'
        ).get(id=subscription_id)
    behind = subscription.messages_behind()
    if behind == 0:
        return
    current_messageset = subscription.messageset
    current_sequence_number = subscription.next_sequence_number
    end_subscription = Subscription.fast_forward_lifecycle(subscription,
        save=False)[-1]
    BehindSubscription.objects.create(subscription=subscription,
        messages_behind=behind, current_messageset=current_messageset,
        current_sequence_number=current_sequence_number,
        expected_messageset=end_subscription.messageset,
        expected_sequence_number=end_subscription.next_sequence_number)