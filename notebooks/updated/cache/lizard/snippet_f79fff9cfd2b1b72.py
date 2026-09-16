def get_prefixes(self, ns_uri):
    ni = self.__lookup_uri(ns_uri)
    return ni.prefixes.copy()