def decrease_posts_count_after_post_unaproval(sender, instance, **kwargs):
    if not instance.pk:
        return
    profile, dummy = ForumProfile.objects.get_or_create(user=instance.poster)
    try:
        old_instance = instance.__class__._default_manager.get(pk=instance.pk)
    except ObjectDoesNotExist:
        return
    if (old_instance and old_instance.approved is True and instance.
        approved is False):
        profile.posts_count = F('posts_count') - 1
        profile.save()