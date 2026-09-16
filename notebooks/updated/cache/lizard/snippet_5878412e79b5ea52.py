def patch_db_connections():
    global __already_patched
    if not __already_patched:
        from django.db import connections
        connections._connections = local(connections._connections)
        __already_patched = True