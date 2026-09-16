def get_object(pid_type, pid_value):
    from .models import PersistentIdentifier
    obj = PersistentIdentifier.get(pid_type, pid_value)
    if obj.has_object():
        click.echo('{0.object_type} {0.object_uuid} {0.status}'.format(obj))