def model_deleted(sender, instance, using, **kwargs):
    opts = get_opts(instance)
    model = '.'.join([opts.app_label, opts.object_name])
    distill_model_event(instance, model, 'deleted')