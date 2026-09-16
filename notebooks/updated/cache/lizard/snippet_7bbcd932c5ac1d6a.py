def lazy_tag(tag, *args, **kwargs):
    tag_id = get_tag_id()
    set_lazy_tag_data(tag_id, tag, args, kwargs)
    return render_to_string('lazy_tags/lazy_tag.html', {'tag_id': tag_id,
        'STATIC_URL': settings.STATIC_URL})