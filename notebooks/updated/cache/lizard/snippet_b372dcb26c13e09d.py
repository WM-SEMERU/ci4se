def load(self, context):
    try:
        import tensorflow
    except ImportError:
        return
    from tensorboard.plugins.hparams.hparams_plugin import HParamsPlugin
    return HParamsPlugin(context)