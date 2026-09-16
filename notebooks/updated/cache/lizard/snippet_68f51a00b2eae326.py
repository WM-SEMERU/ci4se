def set_default_moe_hparams(hparams):
    hparams.moe_num_experts = 16
    hparams.moe_loss_coef = 0.01
    hparams.add_hparam('moe_gating', 'top_2')
    hparams.add_hparam('moe_capacity_factor_train', 1.25)
    hparams.add_hparam('moe_capacity_factor_eval', 2.0)
    hparams.add_hparam('moe_capacity_factor_second_level', 1.0)
    hparams.add_hparam('moe_hidden_size', 4096)
    hparams.add_hparam('moe_group_size', 1024)
    hparams.add_hparam('moe_use_second_place_loss', 0)
    hparams.add_hparam('moe_second_policy_train', 'random')
    hparams.add_hparam('moe_second_policy_eval', 'random')
    hparams.add_hparam('moe_second_threshold_train', 0.2)
    hparams.add_hparam('moe_second_threshold_eval', 0.2)