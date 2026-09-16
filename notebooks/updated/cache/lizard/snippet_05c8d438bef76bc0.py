def format_image_iter(data_fetch, x_start=0, y_start=0, width=32, height=32,
    frame=0, columns=1, downsample=1):
    frames = []
    try:
        frame_iter = iter(frame)
        frames = [f for f in frame_iter]
    except TypeError:
        frames = [frame]
    rows = math.ceil(len(frames) / columns)
    for r in range(rows):
        for y in range(0, height, 2 * downsample):
            result = []
            for c in range(min(len(frames) - r * columns, columns)):
                row = []
                for x in range(0, width, downsample):
                    fr = frames[r * columns + c]
                    c1 = data_fetch(x_start + x, y_start + y, fr)
                    c2 = data_fetch(x_start + x, y_start + y + downsample, fr)
                    row.append((c1, c2))
                prev_pixel = None
                pointer = 0
                while pointer < len(row):
                    start = pointer
                    pixel = row[pointer]
                    while pointer < len(row) and row[pointer] == pixel:
                        pointer += 1
                    result.append(format_pixels(pixel[0], pixel[1], repeat=
                        pointer - start))
            yield ''.join(result)
    return