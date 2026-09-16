def train(self, plot):
    gdefs = []
    for scale in plot.scales:
        for output in scale.aesthetics:
            guide = self.get(output, scale.guide)
            if guide is None or guide is False:
                continue
            guide = self.validate(guide)
            if guide.available_aes != 'any' and scale.aesthetics[0
                ] not in guide.available_aes:
                raise PlotnineError('{} cannot be used for {}'.format(guide
                    .__class__.__name__, scale.aesthetics))
            if is_waive(guide.title):
                if scale.name:
                    guide.title = scale.name
                else:
                    try:
                        guide.title = str(plot.labels[output])
                    except KeyError:
                        warn(
                            'Cannot generate legend for the {!r} aesthetic. Make sure you have mapped a variable to it'
                            .format(output), PlotnineWarning)
                        continue
            guide = guide.train(scale, output)
            if guide is not None:
                gdefs.append(guide)
    return gdefs