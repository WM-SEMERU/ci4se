def valueAt(self, percent):
    minim = self.minimum()
    maxim = self.maximum()
    rtype = self.rulerType()
    if percent <= 0:
        return minim
    elif 1 <= percent:
        return maxim
    elif rtype == XChartRuler.Type.Number:
        return (maxim - minim) * percent
    elif rtype in (XChartRuler.Type.Datetime, XChartRuler.Type.Time):
        maxsecs = minim.secsTo(maxim)
        diff = maxssecs * percent
        return minim.addSecs(diff)
    elif rtype == XChartRuler.Type.Date:
        maxdays = minim.daysTo(maxim)
        diff = maxdays * percent
        return minim.addDays(diff)
    else:
        perc = 0.0
        notches = self.notches()
        count = len(notches)
        count += self.padStart() + self.padEnd()
        count = max(1, count - 1)
        perc = float(self.padStart()) / count
        last = None
        for i, notch in enumerate(notches):
            perc += float(i) / count
            if perc <= percent:
                break
            last = notch
        return last