def manager_post_save_handler(sender, instance, created, **kwargs):
    if (instance.status == Data.STATUS_DONE or instance.status == Data.
        STATUS_ERROR or created):
        transaction.on_commit(lambda : commit_signal(instance.id))