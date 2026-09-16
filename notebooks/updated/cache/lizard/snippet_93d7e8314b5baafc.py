def prepare_defenses(self):
    print_header('PREPARING DEFENSE DATA')
    if not self.ask_when_work_is_populated(self.defense_work):
        return
    self.defense_work = eval_lib.DefenseWorkPieces(datastore_client=self.
        datastore_client)
    self.submissions.init_from_datastore()
    self.dataset_batches.init_from_datastore()
    self.adv_batches.init_from_datastore()
    self.attack_work.read_all_from_datastore()
    print_header('Initializing classification batches')
    self.class_batches.init_from_adversarial_batches_write_to_datastore(self
        .submissions, self.adv_batches)
    if self.verbose:
        print(self.class_batches)
    print_header('Preparing defense work pieces')
    self.defense_work.init_from_class_batches(self.class_batches.data,
        num_shards=self.num_defense_shards)
    self.defense_work.write_all_to_datastore()
    if self.verbose:
        print(self.defense_work)