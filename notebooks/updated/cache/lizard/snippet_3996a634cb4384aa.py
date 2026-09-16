def similar_items(self, itemid, N=10):
    if itemid >= self.similarity.shape[0]:
        return []
    return sorted(list(nonzeros(self.similarity, itemid)), key=lambda x: -x[1]
        )[:N]