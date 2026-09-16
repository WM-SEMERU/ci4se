def _dispatch(self):
    for ingredient in self.ingredients:
        result = ingredient.dispatch(self.context)
        if result is not None:
            return result