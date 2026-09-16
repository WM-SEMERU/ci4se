def _realToVisibleColumn(self, text, realColumn):
    generator = self._visibleCharPositionGenerator(text)
    for i in range(realColumn):
        val = next(generator)
    val = next(generator)
    return val