def get_max_similar(string, lst):
    max_similarity, index = 0.0, -1
    for i, candidate in enumerate(lst):
        sim = how_similar_are(str(string), str(candidate))
        if sim > max_similarity:
            max_similarity, index = sim, i
    return max_similarity, index