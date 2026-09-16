def add_experiment_choice(experiment, choice):
    redis = oz.redis.create_connection()
    oz.bandit.Experiment(redis, experiment).add_choice(choice)