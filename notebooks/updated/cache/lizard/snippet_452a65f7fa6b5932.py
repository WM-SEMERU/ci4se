def get_review_average(obj):
    total = 0
    reviews = get_reviews(obj)
    if not reviews:
        return False
    for review in reviews:
        average = review.get_average_rating()
        if average:
            total += review.get_average_rating()
    if total > 0:
        return total / reviews.count()
    return False