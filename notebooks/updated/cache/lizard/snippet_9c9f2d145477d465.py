def roll_out_and_store(self, batch_info):
    self.model.train()
    if self.env_roller.is_ready_for_sampling():
        rollout = self.env_roller.rollout(batch_info, self.model, self.
            settings.rollout_steps).to_device(self.device)
        batch_info['frames'] = rollout.frames()
        batch_info['episode_infos'] = rollout.episode_information()
    else:
        frames = 0
        episode_infos = []
        with tqdm.tqdm(desc='Populating memory', total=self.env_roller.
            initial_memory_size_hint()) as pbar:
            while not self.env_roller.is_ready_for_sampling():
                rollout = self.env_roller.rollout(batch_info, self.model,
                    self.settings.rollout_steps).to_device(self.device)
                new_frames = rollout.frames()
                frames += new_frames
                episode_infos.extend(rollout.episode_information())
                pbar.update(new_frames)
        batch_info['frames'] = frames
        batch_info['episode_infos'] = episode_infos