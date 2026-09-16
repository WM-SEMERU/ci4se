def exit(self, status=0, message=None):
    if message:
        raise HelpBanner(message.strip(), code=status)