def index_split(index, chunks):
    Ntotal = index.shape[0]
    Nsections = int(chunks)
    if Nsections <= 0:
        raise ValueError('number sections must be larger than 0.')
    Neach_section, extras = divmod(Ntotal, Nsections)
    section_sizes = [0] + extras * [Neach_section + 1] + (Nsections - extras
        ) * [Neach_section]
    div_points = numpy.array(section_sizes).cumsum()
    sub_ind = []
    for i in range(Nsections):
        st = div_points[i]
        end = div_points[i + 1]
        sub_ind.append(index[st:end])
    return sub_ind