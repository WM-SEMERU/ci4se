def makeBubbleChart(self, posdict, name, stattup=None):
    xname = [x for x in name.split('.') if x.startswith('X_')][0]
    yname = [x for x in name.split('.') if x.startswith('Y_')][0]
    o = '<div id="' + name + '"><h2>' + name + '</h2>'
    if stattup:
        cc = stattup[0]
        p = stattup[1]
        o += '<h3>corr.coef=' + str(cc) + ' / p-value=' + str(p) + '</h3>'
    o += (
        '<br/><script type="text/javascript">\nvar myChart = new Chart.Bubble("'
         + name +
        """", {
width: 400,
height: 400,
 bubbleSize: 10,
xlabel:\"""" +
        xname + '",\nylabel:"' + yname + '"});\n')
    for posnum, xydict in posdict.items():
        x_avg, x_std = mean_stdev(xydict['x'])
        y_avg, y_std = mean_stdev(xydict['y'])
        z = 1 / (x_std + y_std)
        o += 'myChart.addBubble(' + str(x_avg * 100) + ', ' + str(y_avg * 100
            ) + ', ' + str(z) + ', "#666", "' + str(posnum + 1) + ' [%' + str(
            x_avg * 100)[0:5] + ', %' + str(y_avg * 100)[0:5] + ']");\n'
    o += 'myChart.redraw();\n</script>\n</div>'
    return o