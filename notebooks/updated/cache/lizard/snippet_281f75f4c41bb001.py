def file_html(models, resources, title=None, template=FILE,
    template_variables={}, theme=FromCurdoc, suppress_callback_warning=
    False, _always_new=False):
    if isinstance(models, Model):
        models = [models]
    if isinstance(models, Document):
        models = models.roots
    with OutputDocumentFor(models, apply_theme=theme, always_new=_always_new
        ) as doc:
        docs_json, render_items = standalone_docs_json_and_render_items(models,
            suppress_callback_warning=suppress_callback_warning)
        title = _title_from_models(models, title)
        bundle = bundle_for_objs_and_resources([doc], resources)
        return html_page_for_render_items(bundle, docs_json, render_items,
            title=title, template=template, template_variables=
            template_variables)