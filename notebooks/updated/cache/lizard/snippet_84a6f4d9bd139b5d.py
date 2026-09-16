def traverse_ingredients(self):
    if self._is_traversing:
        raise CircularDependencyError(ingredients=[self])
    else:
        self._is_traversing = True
    yield self, 0
    with CircularDependencyError.track(self):
        for ingredient in self.ingredients:
            for ingred, depth in ingredient.traverse_ingredients():
                yield ingred, depth + 1
    self._is_traversing = False