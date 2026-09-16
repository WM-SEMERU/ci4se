def calculate_avg_score(res):
    c_star_score = 6
    avg_score = 0.0
    nb_reviews = 0
    for comment in res:
        if comment[c_star_score] > 0:
            avg_score += comment[c_star_score]
            nb_reviews += 1
    if nb_reviews == 0:
        return 0.0
    avg_score = avg_score / nb_reviews
    avg_score_unit = avg_score - math.floor(avg_score)
    if avg_score_unit < 0.25:
        avg_score = math.floor(avg_score)
    elif avg_score_unit > 0.75:
        avg_score = math.floor(avg_score) + 1
    else:
        avg_score = math.floor(avg_score) + 0.5
    if avg_score > 5:
        avg_score = 5.0
    return avg_score