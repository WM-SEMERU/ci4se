def _generate_hash(self, lista):
    hash_elements = defaultdict(list)
    for element in lista:
        key = self.similarity_key(element)
        hash_elements[key].append(element)
    return hash_elements