def _handle_sentry(self):
    from sentry_sdk import capture_exception, configure_scope
    from sentry_sdk.utils import capture_internal_exceptions
    with configure_scope() as scope:
        with capture_internal_exceptions():
            from git import Repo
            from renku.cli._git import get_git_home
            from renku.models.datasets import Author
            user = Author.from_git(Repo(get_git_home()))
            scope.user = {'name': user.name, 'email': user.email}
        event_id = capture_exception()
        click.echo(_BUG + 'Recorded in Sentry with ID: {0}\n'.format(
            event_id), err=True)
        raise