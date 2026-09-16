def prepare_attacks(self):
    print_header('PREPARING ATTACKS DATA')
    if not self.ask_when_work_is_populated(self.attack_work):
        return
    self.attack_work = eval_lib.AttackWorkPieces(datastore_client=self.
        datastore_client)
    print_header('Initializing submissions')
    self.submissions.init_from_storage_write_to_datastore()
    if self.verbose:
        print(self.submissions)
    print_header('Initializing dataset batches')
    self.dataset_batches.init_from_storage_write_to_datastore(batch_size=
        self.batch_size, allowed_epsilon=ALLOWED_EPS, skip_image_ids=[],
        max_num_images=self.max_dataset_num_images)
    if self.verbose:
        print(self.dataset_batches)
    print_header('Initializing adversarial batches')
    self.adv_batches.init_from_dataset_and_submissions_write_to_datastore(
        dataset_batches=self.dataset_batches, attack_submission_ids=self.
        submissions.get_all_attack_ids())
    if self.verbose:
        print(self.adv_batches)
    print_header('Preparing attack work pieces')
    self.attack_work.init_from_adversarial_batches(self.adv_batches.data)
    self.attack_work.write_all_to_datastore()
    if self.verbose:
        print(self.attack_work)