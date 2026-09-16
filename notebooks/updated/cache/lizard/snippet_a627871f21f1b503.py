def cache(self, name, cache_class=Cache, identity_generator_class=
    IdentityGenerator, compressor_class=Compressor, serializer_class=
    Serializer, *args, **kwargs):
    return cache_class(self, *args, app=name, identity_generator_class=
        identity_generator_class, compressor_class=compressor_class,
        serializer_class=serializer_class, **kwargs)