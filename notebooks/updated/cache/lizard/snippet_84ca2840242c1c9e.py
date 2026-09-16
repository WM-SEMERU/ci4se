def get_celery_app(name=None, **kwargs):
    from celery import Celery
    prepare_environment(**kwargs)
    name = name or os.getenv('VST_PROJECT')
    celery_app = Celery(name)
    celery_app.config_from_object('django.conf:settings', namespace='CELERY')
    celery_app.autodiscover_tasks()
    return celery_app