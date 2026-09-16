def autogroups_states_changed(sender, instance, action, reverse, model,
    pk_set, *args, **kwargs):
    if action.startswith('post_'):
        for pk in pk_set:
            try:
                state = State.objects.get(pk=pk)
                instance.update_group_membership_for_state(state)
            except State.DoesNotExist:
                pass