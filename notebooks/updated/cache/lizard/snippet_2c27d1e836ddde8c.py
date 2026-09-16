def _create_configs(cls, site):
    provider = cls.name
    cls._render_config('wsgi.py', 'wsgi.py', site)
    yaml_template_name = os.path.join(provider, cls.provider_yml_name)
    cls._render_config(cls.provider_yml_name, yaml_template_name, site)
    requirements_filename = 'requirements.txt'
    if site['requirements'] != requirements_filename:
        requirements_template_name = os.path.join(provider,
            requirements_filename)
        cls._render_config(requirements_filename,
            requirements_template_name, site)
    settings_template_name = os.path.join(provider, 'settings_%s.py' % provider
        )
    settings_path = site['django_settings'].replace('.', '/'
        ) + '_%s.py' % provider
    cls._render_config(settings_path, settings_template_name, site)