def copy(self, src, dst, other_system=None):
    container, obj = self.split_locator(src)
    with _handle_client_exception():
        self.client.copy_object(container=container, obj=obj, destination=
            self.relpath(dst))