def call(self, tag_name: str, *args, **kwargs):
    if hasattr(self, tag_name):
        getattr(self, tag_name)(*args, **kwargs)