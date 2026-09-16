def post_command(self, sender, name, result, args, kwargs):
    return self._instance.post_command(sender=self, name=name, result=
        result, args=args, kwargs=kwargs)