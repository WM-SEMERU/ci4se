def identifyModule(self, modout=False):
    x, y = np.mean(self.polygon, 0)
    if modout:
        modout = modOutFromChannel(self.channel)
        mp.text(x, y, '%i-%i' % (modout[0], modout[1]), fontsize=8, ha=
            'center', clip_on=True)
    else:
        mp.text(x, y, '%i' % self.channel, fontsize=8, ha='center', clip_on
            =True)