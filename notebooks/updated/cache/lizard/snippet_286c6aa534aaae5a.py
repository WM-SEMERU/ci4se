def warning(self, request, message, extra_tags='', fail_silently=False):
    add(self.target_name, request, constants.WARNING, message, extra_tags=
        extra_tags, fail_silently=fail_silently)