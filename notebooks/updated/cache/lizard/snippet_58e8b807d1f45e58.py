def instantiate(self, **extra_args):
    input_block = self.input_block.instantiate()
    backbone = self.backbone.instantiate(**extra_args)
    return QStochasticPolicyModel(input_block, backbone, extra_args[
        'action_space'])