def depthfirstsearch(self, function):
    result = function(self)
    if result is not None:
        return result
    for e in self:
        result = e.depthfirstsearch(function)
        if result is not None:
            return result
    return None