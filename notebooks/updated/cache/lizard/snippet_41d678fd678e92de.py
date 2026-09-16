def fetch(weeks, force):
    weeks = get_last_weeks(weeks)
    print(weeks)
    recommender = RecordRecommender(config)
    recommender.fetch_weeks(weeks, overwrite=force)