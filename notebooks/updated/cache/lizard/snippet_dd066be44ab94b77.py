def _get_popularity_baseline(self):
    response = self.__proxy__.get_popularity_baseline()
    from .popularity_recommender import PopularityRecommender
    return PopularityRecommender(response)