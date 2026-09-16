def difference(self, *others):
    if all([isinstance(a, self.__class__) for a in others]):
        return self.client.sdiff([self.name] + [other.name for other in others]
            )
    else:
        othersets = filter(lambda x: isinstance(x, set), others)
        otherTypes = filter(lambda x: isinstance(x, self.__class__), others)
        return self.client.sdiff([self.name] + [other.name for other in
            otherTypes]).difference(*othersets)