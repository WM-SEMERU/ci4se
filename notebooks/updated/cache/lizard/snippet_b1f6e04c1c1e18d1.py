def _collection_default_options(self, name, **kargs):
    wc = (self.write_concern if self.write_concern.acknowledged else
        WriteConcern())
    return self.get_collection(name, codec_options=DEFAULT_CODEC_OPTIONS,
        read_preference=ReadPreference.PRIMARY, write_concern=wc)