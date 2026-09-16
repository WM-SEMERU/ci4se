def _parseSelector(self, src):
    src, selector = self._parseSimpleSelector(src)
    srcLen = len(src)
    while src[:1] not in ('', ',', ';', '{', '}', '[', ']', '(', ')'):
        for combiner in self.SelectorCombiners:
            if src.startswith(combiner):
                src = src[len(combiner):].lstrip()
                break
        else:
            combiner = ' '
        src, selectorB = self._parseSimpleSelector(src)
        if len(src) >= srcLen:
            src = src[1:]
            while src and src[:1] not in ('', ',', ';', '{', '}', '[', ']',
                '(', ')'):
                src = src[1:]
            return src.lstrip(), None
        selector = self.cssBuilder.combineSelectors(selector, combiner,
            selectorB)
    return src.lstrip(), selector