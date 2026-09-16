def _reset_env(self, env: BaseUnityEnvironment):
    if self.meta_curriculum is not None:
        return env.reset(train_mode=self.fast_simulation, config=self.
            meta_curriculum.get_config())
    else:
        return env.reset(train_mode=self.fast_simulation)