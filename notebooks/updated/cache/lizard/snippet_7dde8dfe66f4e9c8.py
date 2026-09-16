def _gradient_rgb_line_from_morph(self, text, morphlist, fore=None, back=
    None, style=None):
    try:
        listlen = len(morphlist)
    except TypeError:
        morphlist = list(morphlist)
        listlen = len(morphlist)
    neededsteps = listlen // len(text)
    iterstep = 1
    if neededsteps > iterstep:
        iterstep = neededsteps
    usevals = morphlist
    if iterstep > 1:
        usevals = [usevals[i] for i in range(0, listlen, iterstep)]
    return ''.join(self._iter_text_wave(text, usevals, fore=fore, back=back,
        style=style, rgb_mode=False))