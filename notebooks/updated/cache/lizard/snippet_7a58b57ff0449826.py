def wrapped_env_maker(environment_id, seed, serial_id,
    disable_reward_clipping=False, disable_episodic_life=False, monitor=
    False, allow_early_resets=False, scale_float_frames=False,
    max_episode_frames=10000, frame_stack=None):
    env = env_maker(environment_id)
    env.seed(seed + serial_id)
    if max_episode_frames is not None:
        env = ClipEpisodeLengthWrapper(env, max_episode_length=
            max_episode_frames)
    if monitor:
        logdir = logger.get_dir() and os.path.join(logger.get_dir(), str(
            serial_id))
    else:
        logdir = None
    env = Monitor(env, logdir, allow_early_resets=allow_early_resets)
    if not disable_episodic_life:
        env = EpisodicLifeEnv(env)
    if 'FIRE' in env.unwrapped.get_action_meanings():
        if disable_episodic_life:
            env = FireEpisodicLifeEnv(env)
        else:
            env = FireResetEnv(env)
    env = WarpFrame(env)
    if scale_float_frames:
        env = ScaledFloatFrame(env)
    if not disable_reward_clipping:
        env = ClipRewardEnv(env)
    if frame_stack is not None:
        env = FrameStack(env, frame_stack)
    return env