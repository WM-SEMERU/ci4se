def create_entry_tag(sender, instance, created, **kwargs):
    from ..models import Entry, EntryTag
    entry = Entry.objects.get_for_model(instance.content_object)[0]
    tag = instance.tag
    if not EntryTag.objects.filter(tag=tag, entry=entry).exists():
        EntryTag.objects.create(tag=tag, entry=entry)