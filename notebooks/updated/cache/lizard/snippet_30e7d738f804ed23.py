def create_pie_chart(self, snapshot, filename=''):
    try:
        from pylab import figure, title, pie, axes, savefig
        from pylab import sum as pylab_sum
    except ImportError:
        return self.nopylab_msg % 'pie_chart'
    if not snapshot.tracked_total:
        return ''
    classlist = []
    sizelist = []
    for k, v in list(snapshot.classes.items()):
        if v['pct'] > 3.0:
            classlist.append(k)
            sizelist.append(v['sum'])
    sizelist.insert(0, snapshot.asizeof_total - pylab_sum(sizelist))
    classlist.insert(0, 'Other')
    title('Snapshot (%s) Memory Distribution' % snapshot.desc)
    figure(figsize=(8, 8))
    axes([0.1, 0.1, 0.8, 0.8])
    pie(sizelist, labels=classlist)
    savefig(filename, dpi=50)
    return self.chart_tag % self.relative_path(filename)