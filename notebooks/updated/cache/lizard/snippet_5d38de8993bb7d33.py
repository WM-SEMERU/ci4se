def _manage(target, extra='', proj_settings=PROJ_SETTINGS):
    local(
        "export PYTHONPATH='' && export DJANGO_SETTINGS_MODULE='%s' && django-admin.py %s %s"
         % (proj_settings, target, extra), capture=False)