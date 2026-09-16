def psh_fire_msg_action_if_new(sender, instance, created, **kwargs):
    if created:
        from message_sender.tasks import send_message
        send_message.apply_async(kwargs={'message_id': str(instance.id)})