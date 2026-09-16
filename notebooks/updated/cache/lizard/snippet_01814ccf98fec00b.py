def unindex_model_on_delete(sender, document, **kwargs):
    if current_app.config.get('AUTO_INDEX'):
        unindex.delay(document)