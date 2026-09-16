def patch_related_object_descriptor_caching(ro_descriptor):


    class NewSingleObjectDescriptor(LanguageCacheSingleObjectDescriptor,
        ro_descriptor.__class__):
        pass
    if django.VERSION[0] == 2:
        ro_descriptor.related.get_cache_name = partial(
            NewSingleObjectDescriptor.get_cache_name, ro_descriptor)
    ro_descriptor.accessor = ro_descriptor.related.get_accessor_name()
    ro_descriptor.__class__ = NewSingleObjectDescriptor