def _plotly_3d_scatter(coords, partition=None):
    from plotly.graph_objs import Scatter3d, Data, Figure, Layout, Line, Margin, Marker
    colourmap = {'A': '#1f77b4', 'B': '#ff7f0e', 'C': '#2ca02c', 'D':
        '#d62728', 'E': '#9467bd', (1): '#1f77b4', (2): '#ff7f0e', (3):
        '#2ca02c', (4): '#d62728', (5): '#9467bd'}
    df = coords.df
    if partition:
        assert len(partition.partition_vector) == df.shape[0]
        labels = [(x + 1) for x in partition.partition_vector]
    else:
        labels = [(1) for _ in range(df.shape[0])]
    x, y, z = df.columns[:3]
    df['Label'] = labels
    colours = [colourmap[lab] for lab in df['Label']]
    trace = Scatter3d(x=df[x], y=df[y], z=df[z], mode='markers', marker=
        Marker(size=9, color=colours, line=Line(color=colours, width=0.5),
        opacity=0.8), text=[str(ix) for ix in df.index])
    data = Data([trace])
    layout = Layout(margin=Margin(l=0, r=0, b=0, t=0), hovermode='x')
    fig = Figure(data=data, layout=layout)
    return fig