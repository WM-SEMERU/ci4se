def crop(gens, seconds=5, cropper=None):
    if hasattr(gens, 'next'):
        gens = gens,
    if cropper == None:
        cropper = lambda gen: itertools.islice(gen, 0, seconds * sampler.
            FRAME_RATE)
    cropped = [cropper(gen) for gen in gens]
    return cropped[0] if len(cropped) == 1 else cropped