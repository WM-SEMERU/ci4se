def PlotFactory(xChart, chart):
    try:
        PlotCls = {qn('c:areaChart'): AreaPlot, qn('c:area3DChart'):
            Area3DPlot, qn('c:barChart'): BarPlot, qn('c:bubbleChart'):
            BubblePlot, qn('c:doughnutChart'): DoughnutPlot, qn(
            'c:lineChart'): LinePlot, qn('c:pieChart'): PiePlot, qn(
            'c:radarChart'): RadarPlot, qn('c:scatterChart'): XyPlot}[
            xChart.tag]
    except KeyError:
        raise ValueError('unsupported plot type %s' % xChart.tag)
    return PlotCls(xChart, chart)