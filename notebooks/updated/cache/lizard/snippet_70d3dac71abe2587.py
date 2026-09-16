def set_legend(self):
    leg = super(Coherence, self).set_legend()
    if leg is not None:
        leg.set_title('Coherence with:')
    return leg