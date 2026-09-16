def run(self):
    device = self.model_config.torch_device()
    env = self.vec_env_factory.instantiate_single(preset='record', seed=
        self.model_config.seed)
    model = self.model_factory.instantiate(action_space=env.action_space).to(
        device)
    training_info = TrainingInfo(start_epoch_idx=self.storage.
        last_epoch_idx(), run_name=self.model_config.run_name)
    self.storage.load(training_info, model)
    model.eval()
    self.run_model(model, env, device)