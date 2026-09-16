def member(self, user, objects=False):
    try:
        member = self.search(uid=user, objects=objects)[0]
    except IndexError:
        return None
    if objects:
        return member
    return member[1]