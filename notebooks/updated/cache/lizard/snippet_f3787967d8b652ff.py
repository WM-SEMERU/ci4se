def js_distance(p, q):
    js_dist = np.sqrt(js_divergence(p, q))
    return js_dist