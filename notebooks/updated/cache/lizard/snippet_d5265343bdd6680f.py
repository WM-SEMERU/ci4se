def shell_django(session: DjangoSession, backend: ShellBackend):
    namespace = {'session': session}
    namespace.update(backend.get_namespace())
    embed(user_ns=namespace, header=backend.header)