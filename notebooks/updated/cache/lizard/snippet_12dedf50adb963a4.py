def clean(context: Context, delete_dependencies: bool=False):
    paths = [context.app.asset_build_path, context.app.
        collected_assets_path, context.app.govuk_templates_path,
        'docker-compose.yml', 'package.json', 'package-lock.json',
        'webpack.config.js']
    context.shell('rm -rf %s' % paths_for_shell(paths))
    context.shell('find %s -name "*.pyc" -or -name __pycache__ -delete' %
        context.app.django_app_name)
    if delete_dependencies:
        context.info('Cleaning app %s dependencies' % context.app.name)
        paths = ['node_modules', 'venv']
        context.shell('rm -rf %s' % paths_for_shell(paths))