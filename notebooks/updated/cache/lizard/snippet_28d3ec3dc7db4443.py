def wrapModel(self, model):
    res = IResource(model, None)
    if res is None:
        frag = INavigableFragment(model)
        fragmentName = getattr(frag, 'fragmentName', None)
        if fragmentName is not None:
            fragDocFactory = self._getDocFactory(fragmentName)
            if fragDocFactory is not None:
                frag.docFactory = fragDocFactory
        if frag.docFactory is None:
            raise CouldNotLoadFromThemes(frag, self._preferredThemes())
        useAthena = isinstance(frag, (athena.LiveFragment, athena.LiveElement))
        return self._wrapNavFrag(frag, useAthena)
    else:
        return res