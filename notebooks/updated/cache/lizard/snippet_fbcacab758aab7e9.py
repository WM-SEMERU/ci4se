def GetServiceVersions(namespace):

    def compare(a, b):
        if a == b:
            return 0
        if b in parentMap[a]:
            return -1
        if a in parentMap[b]:
            return 1
        return (a > b) - (a < b)
    if PY3:
        return sorted([v for v, n in iteritems(serviceNsMap) if n ==
            namespace], key=cmp_to_key(compare))
    else:
        return sorted([v for v, n in iteritems(serviceNsMap) if n ==
            namespace], compare)