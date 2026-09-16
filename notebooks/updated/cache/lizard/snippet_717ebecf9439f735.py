def remove(self, pk):
    pk = str(pk)
    try:
        del self.items[pk]
    except KeyError:
        raise ItemNotInCart(pk=pk)
    self.update()