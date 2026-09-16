def is_empty(self):
    if self.properties:
        return False
    if not self.descendants:
        for header in self.ancestry.headers:
            if header.is_atrule and header.directive != '@media':
                return False
    return True