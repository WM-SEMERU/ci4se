def update_batch_count(instance, **kwargs):
    batch = instance.batch
    count = batch.samples.filter(published=True).count()
    if count != batch.count:
        batch.count = count
        if AUTO_PUBLISH_BATCH:
            batch.published = bool(count)
        batch.save()