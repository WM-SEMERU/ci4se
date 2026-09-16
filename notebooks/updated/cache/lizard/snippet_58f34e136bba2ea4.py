def extract_density(population, plane='xy', bins=100, neurite_type=
    NeuriteType.basal_dendrite):
    segment_midpoints = get_feat('segment_midpoints', population,
        neurite_type=neurite_type)
    horiz = segment_midpoints[:, ('xyz'.index(plane[0]))]
    vert = segment_midpoints[:, ('xyz'.index(plane[1]))]
    return np.histogram2d(np.array(horiz), np.array(vert), bins=(bins, bins))