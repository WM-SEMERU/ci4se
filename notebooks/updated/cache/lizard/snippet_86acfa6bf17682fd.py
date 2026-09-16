def bulk_create_awards(objects, batch_size=500, post_save_signal=True):
    count = len(objects)
    if not count:
        return
    badge = objects[0].badge
    try:
        Award.objects.bulk_create(objects, batch_size=batch_size)
        if post_save_signal:
            for obj in objects:
                signals.post_save.send(sender=obj.__class__, instance=obj,
                    created=True)
    except IntegrityError:
        logger.error('✘ Badge %s: IntegrityError for %d awards', badge.slug,
            count)