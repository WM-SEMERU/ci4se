def chart_type(cls, plot):
    try:
        chart_type_method = {'AreaPlot': cls._differentiate_area_chart_type,
            'Area3DPlot': cls._differentiate_area_3d_chart_type, 'BarPlot':
            cls._differentiate_bar_chart_type, 'BubblePlot': cls.
            _differentiate_bubble_chart_type, 'DoughnutPlot': cls.
            _differentiate_doughnut_chart_type, 'LinePlot': cls.
            _differentiate_line_chart_type, 'PiePlot': cls.
            _differentiate_pie_chart_type, 'RadarPlot': cls.
            _differentiate_radar_chart_type, 'XyPlot': cls.
            _differentiate_xy_chart_type}[plot.__class__.__name__]
    except KeyError:
        raise NotImplementedError('chart_type() not implemented for %s' %
            plot.__class__.__name__)
    return chart_type_method(plot)