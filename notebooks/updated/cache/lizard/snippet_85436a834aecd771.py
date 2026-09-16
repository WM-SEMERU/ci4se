def export_context(target_zip):
    from django_productline import utils
    context_file = tasks.get_context_path()
    return utils.create_or_append_to_zip(context_file, target_zip,
        'context.json')