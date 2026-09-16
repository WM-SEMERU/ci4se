def open(filename, frame='unspecified'):
    data = Image.load_data(filename)
    return SegmentationImage(data, frame)