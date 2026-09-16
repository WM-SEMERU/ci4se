def add_experiment(experiment):
    redis = oz.redis.create_connection()
    oz.bandit.add_experiment(redis, experiment)