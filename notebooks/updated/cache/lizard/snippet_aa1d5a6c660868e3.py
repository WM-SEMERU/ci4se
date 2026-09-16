def load(self, context):
    try:
        import tensorflow
        from tensorflow.python.eager import profiler_client
    except ImportError:
        return
    from tensorboard.plugins.profile.profile_plugin import ProfilePlugin
    return ProfilePlugin(context)