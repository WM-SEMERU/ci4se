def build_settings_docs(docs_path, prefix=None):
    dynamic = '[dynamic]'
    lines = ['.. THIS DOCUMENT IS AUTO GENERATED VIA conf.py']
    for name in sorted(registry.keys()):
        if prefix and not name.startswith(prefix):
            continue
        setting = registry[name]
        settings_name = '``%s``' % name
        settings_label = '.. _%s:' % name
        setting_default = setting['default']
        if isinstance(setting_default, str):
            if gethostname() in setting_default or setting_default.startswith(
                '/') and os.path.exists(setting_default):
                setting_default = dynamic
        if setting_default != dynamic:
            setting_default = repr(deep_force_unicode(setting_default))
        lines.extend(['', settings_label])
        lines.extend(['', settings_name, '-' * len(settings_name)])
        lines.extend(['', urlize(setting['description'] or '').replace(
            '<a href="', '`').replace('" rel="nofollow">', ' <').replace(
            '</a>', '>`_')])
        if setting['choices']:
            choices = ', '.join([('%s: ``%s``' % (str(v), force_text(k))) for
                k, v in setting['choices']])
            lines.extend(['', 'Choices: %s' % choices, ''])
        lines.extend(['', 'Default: ``%s``' % setting_default])
    with open(os.path.join(docs_path, 'settings.rst'), 'w') as f:
        f.write('\n'.join(lines).replace("u'", "'").replace("yo'", "you'").
            replace('&#39;', "'"))