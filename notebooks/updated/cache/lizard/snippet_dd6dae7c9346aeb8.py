def validate(self, dist):
    for item in self.remove:
        if not dist.has_contents_for(item):
            raise DistutilsSetupError(
                "%s wants to be able to remove %s, but the distribution doesn't contain any packages or modules under %s"
                 % (self.description, item, item))