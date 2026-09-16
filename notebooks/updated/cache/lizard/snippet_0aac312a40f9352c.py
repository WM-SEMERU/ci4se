def colorate(sequence, colormap='', start=0, length=None):
    n = start
    colors = color_space(colormap, sequence, start=0.1, stop=0.9, length=length
        )
    for elem in sequence:
        yield n, colors[n - start], elem
        n += 1